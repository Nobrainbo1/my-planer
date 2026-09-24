"""Regression checks for broken handoffs and accidental audit-artifact creation."""

import contextlib
import io
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from verify_links import CORE_DOCUMENTATION_FILES, run_scanner


class LinkChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def scan(self, files):
        with contextlib.redirect_stdout(io.StringIO()):
            return run_scanner(self.root, files)

    def test_resolves_link_relative_to_source_and_checks_anchor(self):
        self.write("docs/plan.md", "[Task](../tasks.md#first-task)\n")
        self.write("tasks.md", "# First task\n")
        self.assertTrue(self.scan(["docs/plan.md"])["passed"])
        self.write("tasks.md", "# Different task\n")
        result = self.scan(["docs/plan.md"])
        self.assertFalse(result["passed"])
        self.assertEqual(result["details"][0]["status"], "BROKEN_ANCHOR")

    def test_missing_handoff_target_fails(self):
        self.write("plan.md", "[Missing](missing.md)\n")
        result = self.scan(["plan.md"])
        self.assertFalse(result["passed"])
        self.assertEqual(result["details"][0]["status"], "BROKEN_PATH")

    def test_missing_source_fails(self):
        result = self.scan(["missing.md"])
        self.assertFalse(result["passed"])
        self.assertEqual(result["missing_source_files"], ["missing.md"])

    def test_fenced_examples_are_not_live_links(self):
        self.write("plan.md", "```text\n[Example](nonexistent.md)\n```\n")
        result = self.scan(["plan.md"])
        self.assertTrue(result["passed"])
        self.assertEqual(result["total_links_found"], 0)

    def test_external_syntax_is_not_claimed_as_verified(self):
        self.write("plan.md", "[External](https://example.invalid/unknown)\n")
        result = self.scan(["plan.md"])
        self.assertEqual(result["details"][0]["status"], "UNCHECKED_EXTERNAL")
        self.assertIsNone(result["details"][0]["target_exists"])

    def test_cli_is_read_only_by_default_and_json_is_opt_in(self):
        for name in CORE_DOCUMENTATION_FILES:
            self.write(name, "# Fixture\n")
        script = Path(__file__).with_name("verify_links.py")
        command = [sys.executable, "-B", str(script), "--root", str(self.root)]
        before = set(self.root.rglob("*"))
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(before, set(self.root.rglob("*")))
        report = self.root / "report.json"
        result = subprocess.run(command + ["--output-json", str(report)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertTrue(report.is_file())
        self.assertFalse((self.root / ".agents/orchestrator_1").exists())


if __name__ == "__main__":
    unittest.main()
