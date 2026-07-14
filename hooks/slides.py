"""Build Reveal.js slides from resources/slides into site/slides for mkdocs serve."""

from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "resources" / "slides"
MARKER = "{{MARKDOWN_CONTENT}}"
PRIMARY_DECK = "brain-to-image-editing-introduction.md"


def on_post_build(config, **kwargs) -> None:
    if not SRC.exists():
        return

    site_slides = Path(config["site_dir"]) / "slides"
    if site_slides.exists():
        shutil.rmtree(site_slides)
    site_slides.mkdir(parents=True)

    template_path = SRC / "index.html"
    if not template_path.exists():
        shutil.copytree(SRC, site_slides, dirs_exist_ok=True)
        return

    template = template_path.read_text(encoding="utf-8")

    for md_file in sorted(SRC.glob("*.md")):
        md_content = md_file.read_text(encoding="utf-8")
        html = template.replace(MARKER, md_content)

        outputs = [f"{md_file.stem}.html"]
        if md_file.name == PRIMARY_DECK:
            outputs.insert(0, "index.html")

        for output_name in outputs:
            (site_slides / output_name).write_text(html, encoding="utf-8")
