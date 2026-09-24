#!/usr/bin/env python3
"""
verify_links.py — Automated Programmatic Link & Reference Integrity Scanner

Scans maintained documentation for inline Markdown links and heading anchors.
This is a lightweight checker, not a complete Markdown parser. It does not parse
reference-style links or fetch external URLs.

Outputs a human-readable console summary and structured JSON results.
"""

import argparse
import json
import os
from pathlib import Path
import re
import sys
from typing import Any, Dict, List, Optional, Set, Tuple
from urllib.parse import urlparse


# Explicit entrypoints also detect accidentally deleted maintained documents.
CORE_DOCUMENTATION_FILES = [
    "README.md",
    ".agents/AGENTS.md",
    ".agents/skills/grill-with-docs/SKILL.md",
    ".agents/skills/planner/SKILL.md",
    ".agents/skills/planner/references/01_DISCOVERY.md",
    ".agents/skills/planner/references/02_PLANNING.md",
    ".agents/skills/planner/references/03_TOOLING.md",
    ".agents/skills/planner/references/HANDOFF.md",
    ".agents/skills/planner/references/EVALUATION.md",
    ".agents/skills/planner/resources/templates/execution_plan.md",
    ".agents/skills/planner/resources/templates/setup.md",
]


def github_slug(heading_text: str) -> str:
    """
    Computes GitHub-compatible anchor slug for a markdown heading.
    Removes inline markdown formatting (backticks, links, bold/italics),
    strips punctuation, converts spaces to hyphens, and lowercases.
    """
    # Remove link formatting [text](url) -> text
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', heading_text)
    # Remove image formatting ![alt](url) -> alt
    text = re.sub(r'!\[([^\]]*)\]\([^)]+\)', r'\1', text)
    # Remove backticks, asterisks, underscores, strikethroughs
    text = re.sub(r'[`*_~]', '', text)
    # Lowercase
    slug = text.strip().lower()
    # Strip non-alphanumeric, non-space, non-hyphen (e.g. '.', ',', '(', ')', '&', '—')
    # Note: Em-dash '—' and ampersand '&' stripped leaving adjacent spaces intact
    slug = re.sub(r'[^\w\s-]', '', slug)
    # Convert each whitespace character to a hyphen
    slug = re.sub(r'\s', '-', slug)
    return slug


def extract_headings(file_path: Path) -> List[Tuple[int, str, str]]:
    """
    Extracts all markdown headings from a file.
    Returns list of (line_number, heading_text, slug).
    """
    headings = []
    if not file_path.is_file():
        return headings

    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception:
        return headings

    in_code_block = False
    for line_num, line in enumerate(content.splitlines(), start=1):
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue

        match = re.match(r'^(#{1,6})\s+(.+)$', stripped)
        if match:
            heading_text = match.group(2).strip()
            slug = github_slug(heading_text)
            headings.append((line_num, heading_text, slug))

    return headings


def find_markdown_links(file_path: Path) -> List[Dict[str, Any]]:
    """
    Parses a markdown file and extracts all markdown links and targets.
    Excludes links located inside fenced code blocks.
    """
    links = []
    if not file_path.is_file():
        return links

    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Error reading {file_path}: {e}", file=sys.stderr)
        return links

    in_code_block = False
    # Regular expressions for markdown links
    # Matches [link text](url_or_path "optional title")
    inline_link_pattern = re.compile(r'!?\[([^\]]*)\]\(\s*([^\s\)\"]+)(?:\s+["\'][^"\']*["\'])?\s*\)')

    for line_num, line in enumerate(content.splitlines(), start=1):
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue

        for match in inline_link_pattern.finditer(line):
            text = match.group(1)
            raw_target = match.group(2).strip()
            # Clean possible surrounding angle brackets <url>
            if raw_target.startswith("<") and raw_target.endswith(">"):
                raw_target = raw_target[1:-1].strip()

            links.append({
                "source_file": str(file_path),
                "line_number": line_num,
                "text": text,
                "raw_target": raw_target,
            })

    return links


def classify_and_verify_link(
    link_info: Dict[str, Any],
    source_file_path: Path,
    repo_root: Path,
    cached_headings: Dict[Path, List[Tuple[int, str, str]]],
) -> Dict[str, Any]:
    """
    Classifies link (external, pure anchor, relative path, relative path with anchor)
    and verifies filesystem resolution and anchor existence.
    """
    raw_target = link_info["raw_target"]
    line_num = link_info["line_number"]
    text = link_info["text"]

    parsed = urlparse(raw_target)
    is_external = bool(parsed.scheme in ("http", "https", "mailto", "ftp"))

    result = {
        "source_file": str(source_file_path.relative_to(repo_root)).replace("\\", "/"),
        "line_number": line_num,
        "link_text": text,
        "target": raw_target,
        "is_external": is_external,
        "type": "external" if is_external else "relative",
        "resolved_path": None,
        "target_exists": None,
        "anchor": None,
        "anchor_exists": None,
        "status": "UNKNOWN",
        "error_message": None,
    }

    if is_external:
        # Validate external URL structure
        if parsed.netloc or parsed.path:
            result["status"] = "UNCHECKED_EXTERNAL"
        else:
            result["status"] = "INVALID_EXTERNAL_SYNTAX"
            result["target_exists"] = False
            result["error_message"] = "Malformed external URL"
        return result

    # Handle internal/relative links
    # Check if target contains an anchor
    path_part = raw_target
    anchor_part = None
    if "#" in raw_target:
        parts = raw_target.split("#", 1)
        path_part = parts[0]
        anchor_part = parts[1]
        result["anchor"] = anchor_part

    # 1. Pure anchor link within the same document: e.g. #heading-name
    if not path_part and anchor_part:
        result["type"] = "anchor_only"
        target_file = source_file_path.resolve()
        result["resolved_path"] = str(target_file.relative_to(repo_root)).replace("\\", "/")
        result["target_exists"] = True

        if target_file not in cached_headings:
            cached_headings[target_file] = extract_headings(target_file)

        heading_slugs = [h[2] for h in cached_headings[target_file]]
        if anchor_part in heading_slugs:
            result["anchor_exists"] = True
            result["status"] = "VALID"
        else:
            result["anchor_exists"] = False
            result["status"] = "BROKEN_ANCHOR"
            result["error_message"] = f"Anchor '#{anchor_part}' not found in {result['resolved_path']}"
        return result

    # 2. Relative file/directory path (possibly with an anchor)
    # Resolve relative to the source file's directory
    target_path = (source_file_path.parent / path_part).resolve()
    try:
        rel_to_repo = str(target_path.relative_to(repo_root)).replace("\\", "/")
    except ValueError:
        rel_to_repo = str(target_path).replace("\\", "/")

    result["resolved_path"] = rel_to_repo
    target_exists = target_path.exists()
    result["target_exists"] = target_exists

    if not target_exists:
        result["status"] = "BROKEN_PATH"
        result["error_message"] = f"Target file or directory does not exist: {rel_to_repo}"
        return result

    # Target path exists on disk
    if anchor_part:
        result["type"] = "relative_with_anchor"
        if target_path not in cached_headings:
            cached_headings[target_path] = extract_headings(target_path)

        heading_slugs = [h[2] for h in cached_headings[target_path]]
        if anchor_part in heading_slugs:
            result["anchor_exists"] = True
            result["status"] = "VALID"
        else:
            result["anchor_exists"] = False
            result["status"] = "BROKEN_ANCHOR"
            result["error_message"] = f"Anchor '#{anchor_part}' not found in target file: {rel_to_repo}"
    else:
        result["type"] = "relative_path"
        result["status"] = "VALID"

    return result


def run_scanner(
    repo_root: Path,
    target_files: Optional[List[str]] = None,
    output_json_path: Optional[Path] = None,
    verbose: bool = False,
) -> Dict[str, Any]:
    """
    Executes the link scanner over specified markdown files or the entire repository.
    """
    if target_files is None:
        target_files = CORE_DOCUMENTATION_FILES

    resolved_files: List[Path] = []
    missing_files: List[str] = []

    for rel_path in target_files:
        p = repo_root / rel_path
        if p.is_file():
            resolved_files.append(p)
        else:
            missing_files.append(rel_path)

    cached_headings: Dict[Path, List[Tuple[int, str, str]]] = {}
    verified_links: List[Dict[str, Any]] = []

    for file_path in resolved_files:
        extracted = find_markdown_links(file_path)
        for link_info in extracted:
            v = classify_and_verify_link(link_info, file_path, repo_root, cached_headings)
            verified_links.append(v)

    # Statistics calculation
    total_files_scanned = len(resolved_files)
    total_links_found = len(verified_links)

    relative_links = [l for l in verified_links if not l["is_external"]]
    external_links = [l for l in verified_links if l["is_external"]]
    anchor_links = [l for l in verified_links if l["anchor"] is not None]

    broken_links = [l for l in verified_links if l["status"] in ("BROKEN_PATH", "BROKEN_ANCHOR", "INVALID_EXTERNAL_SYNTAX")]

    is_passed = (len(broken_links) == 0 and len(missing_files) == 0)

    summary = {
        "total_files_scanned": total_files_scanned,
        "missing_source_files_count": len(missing_files),
        "missing_source_files": missing_files,
        "total_links_found": total_links_found,
        "total_relative_links": len(relative_links),
        "total_anchor_links": len(anchor_links),
        "total_external_links": len(external_links),
        "broken_links_count": len(broken_links),
        "passed": is_passed,
        "details": verified_links,
    }

    # Print human-readable summary
    print("=" * 75)
    print("  AUTOMATED PROGRAMMATIC LINK & REFERENCE INTEGRITY SCANNER")
    print("=" * 75)
    print(f"Repository Root        : {repo_root}")
    print(f"Core Files Target List : {len(target_files)} specified")
    print(f"Files Found & Scanned  : {total_files_scanned}")
    if missing_files:
        print(f"MISSING Core Files     : {len(missing_files)} ({', '.join(missing_files)})")
    print(f"Total Markdown Links   : {total_links_found}")
    print(f"  - Relative Links     : {len(relative_links)}")
    print(f"  - Intra-Doc Anchors  : {len(anchor_links)}")
    print(f"  - External URLs      : {len(external_links)}")
    print("-" * 75)
    print(f"Broken Links Detected  : {len(broken_links)}")
    print(f"Verification Result    : {'PASSED (0 Broken Links)' if is_passed else 'FAILED'}")
    print("=" * 75)

    if broken_links:
        print("\n[!] DETECTED BROKEN LINKS:")
        for bl in broken_links:
            print(f"  • {bl['source_file']}:{bl['line_number']} -> '{bl['target']}'")
            print(f"    Status: {bl['status']} | Error: {bl['error_message']}")

    if verbose:
        print("\n--- Detailed Scan Breakdown ---")
        for idx, lk in enumerate(relative_links, start=1):
            anchor_desc = f" (Anchor: #{lk['anchor']})" if lk['anchor'] else ""
            print(f"{idx:02d}. [{lk['status']}] {lk['source_file']}:{lk['line_number']} -> {lk['target']}{anchor_desc}")

    # Write JSON output if requested
    if output_json_path:
        output_json_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_json_path, "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2)
        print(f"\nJSON scan results successfully written to: {output_json_path}")

    return summary


def main():
    parser = argparse.ArgumentParser(
        description="Verify markdown relative links and heading anchors across template_workflow."
    )
    parser.add_argument(
        "--root",
        type=str,
        default=None,
        help="Path to repository root. Defaults to parent directory of scripts/.",
    )
    parser.add_argument(
        "--output-json",
        type=str,
        default=None,
        help="Optional path to output JSON results.",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Print verbose listing of all scanned links.",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Scan all Markdown files, excluding .git, node_modules, and Python caches.",
    )

    args = parser.parse_args()

    if args.root:
        repo_root = Path(args.root).resolve()
    else:
        # Default: script is at scripts/verify_links.py -> repo root is parent of scripts/
        repo_root = Path(__file__).resolve().parent.parent

    target_files = None
    if args.all:
        all_md = []
        for p in repo_root.rglob("*.md"):
            # Exclude .git and node_modules
            rel = str(p.relative_to(repo_root)).replace("\\", "/")
            if not {".git", "node_modules", "__pycache__"}.intersection(p.relative_to(repo_root).parts):
                all_md.append(rel)
        target_files = sorted(all_md)

    output_json = Path(args.output_json).resolve() if args.output_json else None

    summary = run_scanner(
        repo_root=repo_root,
        target_files=target_files,
        output_json_path=output_json,
        verbose=args.verbose,
    )

    sys.exit(0 if summary["passed"] else 1)


if __name__ == "__main__":
    main()
