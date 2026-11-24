# Bebé en Camino

A bite-sized course for first-time parents (in Spanish), published with GitHub Pages.

- `guia-bebe.html` is the source page (also published as a claude.ai artifact).
- `scripts/build_site.py` builds the static site into `docs/`, which GitHub Pages serves.

Rebuild after editing the source:

```sh
python3 scripts/build_site.py
```

General information only; it does not replace advice from a midwife or paediatrician.

`assets/` holds the self-hosted fonts and PNG app icons the build copies into `docs/`; the build also writes a service worker (`docs/sw.js`) so the installed site works offline.
