"""Validate documentation links and keep private records out of the source tree."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote

root = Path(__file__).resolve().parents[1]
required = {
    "getting-started", "desktop-workflow", "cli-automation", "model-server",
    "schema-review", "privacy-and-data", "updates", "troubleshooting",
    "benchmark-gate", "openwiki",
}
errors = []
for name in required:
    if not (root / "docs" / f"{name}.md").is_file():
        errors.append(f"Missing guide: {name}")
for path in root.rglob("*"):
    if ".git" in path.relative_to(root).parts or not path.is_file():
        continue
    if path.suffix.lower() in {".pdf", ".png", ".jpg", ".jpeg", ".xlsx", ".csv", ".gguf", ".sqlite", ".sqlite3", ".exe", ".dll"} or path.name.startswith(".env"):
        errors.append(f"Private/runtime file is not documentation: {path.relative_to(root)}")
markdown = list(root.rglob("*.md"))
for path in markdown:
    text = path.read_text(encoding="utf-8-sig")
    if re.search(r"gh[pousr]_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9_-]{25,}", text):
        errors.append(f"Possible credential in {path.relative_to(root)}")
    for match in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", text):
        target = match.group(1).strip("<>").split("#", 1)[0]
        if not target or re.match(r"[a-z]+:", target):
            continue
        resolved = (path.parent / unquote(target)).resolve()
        if not resolved.is_relative_to(root) or not resolved.is_file():
            errors.append(f"Broken or external local link in {path.relative_to(root)}: {target}")
    if path.parent.name == "docs" and not re.search(r"https://github\.com/[^\s)]+/blob/", text):
        errors.append(f"Guide lacks a source citation: {path.name}")
if errors:
    print("\n".join(errors), file=sys.stderr)
    raise SystemExit(1)
print(f"Checked {len(markdown)} Markdown files: guides, local links, citations and private-file exclusions passed.")
