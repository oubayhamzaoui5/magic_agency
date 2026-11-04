# Les signes Magic

18 original, editable SVG icons authored for Magic 360; no icon font or downloaded icon pack. Eight brand symbols plus ten functional UI controls. Curved geometry, a consistent 32×32 optical frame, 1.6-unit rounded stroke, a pale-gold four-point sparkle and mint/cream fills connect the set to the actual wizard/wand logo without redrawing it.

Source of truth: `website/magic_icons.py`. Rebuild the SVG sprite, individual files and noindex preview through `python website/build_magic.py` from the project root. Do not edit only generated output if changes must survive the next build.

- Main UI uses `assets/magic-icons.svg` via accessible-hidden SVG use elements; adjacent text or button aria-labels convey meaning.
- Standalone SVG files in this folder are reusable vector assets.
- Preview: `http://127.0.0.1:8000/website/icon-preview.html`.
- CSS inherits currentColor for stroke; `--icon-accent` and `--icon-wash` control the secondary fills. Reduced motion suppresses the small hover response.

Brand symbols: brand (identity/printed form), voice (amplification), experience (stage/portal), listen (conversation), wand (ideation), launch (realization), paper (attention to detail), spark (Magic signature).
