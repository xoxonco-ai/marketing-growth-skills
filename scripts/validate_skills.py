"""Validate every .claude/skills/*/SKILL.md frontmatter and compile bundled Python scripts."""
import py_compile
import re
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / ".claude" / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

errors = []
skill_dirs = sorted(p for p in SKILLS.iterdir() if p.is_dir())
for skill in skill_dirs:
    md = skill / "SKILL.md"
    if not md.is_file():
        errors.append(f"{skill.name}: missing SKILL.md")
        continue
    text = md.read_text(encoding="utf-8")
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    if not m:
        errors.append(f"{skill.name}: missing YAML frontmatter")
        continue
    try:
        meta = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as e:
        errors.append(f"{skill.name}: invalid YAML frontmatter: {e}")
        continue
    name = meta.get("name")
    desc = meta.get("description")
    if name != skill.name:
        errors.append(f"{skill.name}: name {name!r} does not match directory")
    elif len(name) > 64 or not NAME_RE.match(name):
        errors.append(f"{skill.name}: name must be 1-64 chars, lowercase letters, digits, single hyphens")
    if not isinstance(desc, str) or not 1 <= len(desc) <= 1024:
        errors.append(f"{skill.name}: description must be a 1-1024 char string")

scripts = sorted(SKILLS.rglob("*.py"))
tmp = tempfile.mkdtemp()
for script in scripts:
    try:
        py_compile.compile(str(script), cfile=str(Path(tmp) / "out.pyc"), doraise=True)
    except py_compile.PyCompileError as e:
        errors.append(f"{script.relative_to(ROOT)}: {e.msg}")

for err in errors:
    print(f"ERROR {err}")
print(f"Checked {len(skill_dirs)} skills and {len(scripts)} Python scripts: {len(errors)} error(s)")
sys.exit(1 if errors else 0)
