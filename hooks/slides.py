"""Generate Reveal.js decks early enough for MkDocs to serve their routes."""

from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "resources" / "slides"
MARKER = "{{MARKDOWN_CONTENT}}"


def on_pre_build(config, **kwargs) -> None:
    if not SRC.exists():
        return

    slides_dir = Path(config["docs_dir"]) / "slides"
    slides_dir.mkdir(parents=True, exist_ok=True)

    template_path = SRC / "index.html"
    if not template_path.exists():
        shutil.copytree(SRC, slides_dir, dirs_exist_ok=True)
        return

    template = template_path.read_text(encoding="utf-8")
    deck_names = {md_file.stem for md_file in SRC.glob("*.md")}

    for deck_dir in slides_dir.iterdir():
        if deck_dir.is_dir() and deck_dir.name not in deck_names:
            shutil.rmtree(deck_dir)

    for md_file in sorted(SRC.glob("*.md")):
        md_content = md_file.read_text(encoding="utf-8")
        html = template.replace(MARKER, md_content)

        deck_dir = slides_dir / md_file.stem
        deck_dir.mkdir(exist_ok=True)
        deck_path = deck_dir / "index.html"
        if not deck_path.exists() or deck_path.read_text(encoding="utf-8") != html:
            deck_path.write_text(html, encoding="utf-8")
