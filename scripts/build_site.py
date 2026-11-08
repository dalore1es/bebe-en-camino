"""Build the static site for GitHub Pages from guia-bebe.html.

guia-bebe.html is authored for the claude.ai artifact viewer, which wraps it in a
document skeleton. This script adds that skeleton (doctype, head, base reset) plus a
web app manifest and icon so the course can be added to a phone's home screen.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "guia-bebe.html"
OUT = ROOT / "docs"
SPLIT_MARKER = '<div class="wrap">'

HEAD_EXTRA = """<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#2f6f8f">
<meta name="description" content="Curso por píldoras para padres primerizos.">
<meta name="robots" content="noindex">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="icon-180.png">
<style>
:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
body{margin:0}
img{max-width:100%}
[hidden]{display:none!important}
</style>
"""

MANIFEST = """{
  "name": "Bebé en Camino",
  "short_name": "Bebé en Camino",
  "lang": "es",
  "start_url": "./",
  "display": "standalone",
  "background_color": "#f3f5f7",
  "theme_color": "#2f6f8f",
  "icons": [
    {"src": "icon.svg", "sizes": "any", "type": "image/svg+xml"},
    {"src": "icon-180.png", "sizes": "180x180", "type": "image/png"}
  ]
}
"""

ICON_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 180">
<rect width="180" height="180" rx="40" fill="#2f6f8f"/>
<circle cx="70" cy="86" r="34" fill="#f1dcc4"/>
<path d="M36 86a34 34 0 0 1 22-32q-9 18-5 32q-4 14 5 32a34 34 0 0 1-22-32z" fill="#8a5a2c"/>
<rect x="96" y="62" width="58" height="48" rx="20" fill="#f3f5f7"/>
<rect x="40" y="132" width="100" height="10" rx="5" fill="#b76a1f"/>
</svg>
"""


def main() -> None:
    source = SOURCE.read_text(encoding="utf-8")
    head_part, sep, body_part = source.partition(SPLIT_MARKER)
    if not sep:
        raise SystemExit(f"Marker {SPLIT_MARKER!r} not found in {SOURCE.name}")
    # The artifact-only viewport hint is meaningless outside claude.ai.
    head_part = head_part.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', "")
    html = (
        "<!doctype html>\n<html lang=\"es\">\n<head>\n"
        + HEAD_EXTRA
        + head_part.strip()
        + "\n</head>\n<body>\n"
        + SPLIT_MARKER
        + body_part.rstrip()
        + "\n</body>\n</html>\n"
    )
    OUT.mkdir(exist_ok=True)
    (OUT / "index.html").write_text(html, encoding="utf-8")
    (OUT / "manifest.webmanifest").write_text(MANIFEST, encoding="utf-8")
    (OUT / "icon.svg").write_text(ICON_SVG, encoding="utf-8")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    print(f"Built {OUT / 'index.html'} ({len(html) // 1024} KB)")


if __name__ == "__main__":
    main()
