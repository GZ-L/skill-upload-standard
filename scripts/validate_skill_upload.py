#!/usr/bin/env python3
"""Validate that a Skill repository has professional upload documentation."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


README_SECTIONS = {
    "what": [r"这是什么", r"what\s+this\s+is", r"overview"],
    "source": [r"来源", r"source", r"归属", r"ownership"],
    "when": [r"适用场景", r"when\s+to\s+use", r"trigger"],
    "effect": [r"效果", r"能力", r"capabilities", r"expected\s+results"],
    "install": [r"安装", r"install"],
    "usage": [r"使用", r"usage"],
    "validation": [r"验证", r"validation", r"test"],
    "limits": [r"边界", r"注意事项", r"limitations", r"safety"],
    "license": [r"许可证", r"版权", r"license", r"notice"],
}

SECRET_PATTERNS = [
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
    re.compile(r"(?i)\b(api[_-]?key|secret|token|password)\s*=\s*['\"][^'\"]{12,}['\"]"),
    re.compile(r"gho_[A-Za-z0-9_]{20,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def has_any(text: str, patterns: list[str]) -> bool:
    return any(re.search(pattern, text, re.IGNORECASE) for pattern in patterns)


def validate_skill_md(root: Path, errors: list[str], warnings: list[str]) -> None:
    skill_path = root / "SKILL.md"
    if not skill_path.exists():
        errors.append("Missing SKILL.md at repository root.")
        return

    text = read_text(skill_path)
    if not text.startswith("---"):
        errors.append("SKILL.md must start with YAML frontmatter.")
        return

    match = re.match(r"---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        errors.append("SKILL.md frontmatter is not closed with ---.")
        return

    frontmatter = match.group(1)
    name_match = re.search(r"^name:\s*([a-z0-9][a-z0-9-]*)\s*$", frontmatter, re.MULTILINE)
    description_match = re.search(r"^description:\s*(.+)$", frontmatter, re.MULTILINE)

    if not name_match:
        errors.append("SKILL.md frontmatter needs lowercase hyphen-case name.")

    if not description_match:
        errors.append("SKILL.md frontmatter needs description.")
    else:
        description = description_match.group(1)
        if len(description) < 80:
            warnings.append("SKILL.md description is short; include capability, triggers, and exclusions.")
        if not re.search(r"Use when|when the user|使用|触发|says", description, re.IGNORECASE):
            warnings.append("SKILL.md description should include trigger scenarios or user phrases.")
        if not re.search(r"Do not use|不适用|不要用于|not use", description, re.IGNORECASE):
            warnings.append("SKILL.md description should include non-use cases.")

    body = text[match.end():]
    for label, pattern in {
        "workflow": r"workflow|工作流|流程",
        "validation": r"validation|验证",
        "resource routing": r"resource routing|资源路由|references/",
    }.items():
        if not re.search(pattern, body, re.IGNORECASE):
            warnings.append(f"SKILL.md should include {label}.")


def validate_readme(root: Path, errors: list[str], warnings: list[str]) -> None:
    readme_path = root / "README.md"
    if not readme_path.exists():
        errors.append("Missing README.md.")
        return

    text = read_text(readme_path)
    if len(text.strip()) < 800:
        warnings.append("README.md is short for a professional GitHub Skill upload.")

    missing = [key for key, patterns in README_SECTIONS.items() if not has_any(text, patterns)]
    if missing:
        errors.append("README.md missing required topic(s): " + ", ".join(missing))

    if "```" not in text:
        warnings.append("README.md should include copy-pastable command or usage examples.")

    if not re.search(r"SKILL\.md", text):
        warnings.append("README.md should mention SKILL.md or explain the Skill entrypoint.")


def validate_notice(root: Path, warnings: list[str]) -> None:
    readme_text = read_text(root / "README.md") if (root / "README.md").exists() else ""
    source_is_complex = re.search(
        r"改造|对标|上游|第三方|source|upstream|license|redistribut",
        readme_text,
        re.IGNORECASE,
    )
    if source_is_complex and not (root / "NOTICE.md").exists():
        warnings.append("Source/licensing looks non-trivial; consider adding NOTICE.md.")


def scan_for_secrets(root: Path, errors: list[str]) -> None:
    ignored_dirs = {".git", "node_modules", ".venv", "dist", "build", ".next"}
    for path in root.rglob("*"):
        if path.is_dir():
            continue
        if any(part in ignored_dirs for part in path.parts):
            continue
        if path.stat().st_size > 1_000_000:
            continue
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".webp", ".pdf", ".zip"}:
            continue
        text = read_text(path)
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                errors.append(f"Possible secret found in {path.relative_to(root)}")
                break


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("repo", help="Path to the Skill repository to validate")
    args = parser.parse_args()

    root = Path(args.repo).expanduser().resolve()
    errors: list[str] = []
    warnings: list[str] = []

    if not root.exists() or not root.is_dir():
        print(f"ERROR: not a directory: {root}", file=sys.stderr)
        return 2

    validate_skill_md(root, errors, warnings)
    validate_readme(root, errors, warnings)
    validate_notice(root, warnings)
    scan_for_secrets(root, errors)

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        print(f"FAILED: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1

    print(f"PASSED: 0 error(s), {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
