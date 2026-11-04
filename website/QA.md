# Local verification — 2026-10-28

Scope: exactly five alternative French homepages. Existing static Python server at http://127.0.0.1:8000/. Source builder: `python website/build_homepages.py`; shared CSS/JS under assets/. No package install or build service needed.

## Passed
- Phone-first emulation at 390×844, followed by desktop at 1440×1000; additional narrow phone check at 320×740. All five: no horizontal document overflow, one H1, no unresolved local asset or anchor references, noindex metadata.
- Original nav.png logo and existing green/cream/gold palette retained. Original files preserved; five generated image masters copied into project and 15 responsive WebP files exported (480/900/1400px). Visual contact sheet reviewed for artifacts, cropping and fictional brand text. Generated images are labelled concepts, not client commissions.
- Six existing partner logos retained with original partner relationship label; not attributed to fictional work. Other partner assets remain untouched in repository. No invented testimonial, commercial statistic or delivery-time guarantee.
- All five project dialogs opened on every theme at phone and desktop; full-page gallery images confirmed loaded. Escape closes modal and keyboard focus returns to invoking project button. Explicit close button exists. Dialog contact leads to real contact section.
- All five phone menus open and project navigation closes them. Branding filters return two visible concepts; reset returns the complete gallery. Native service details open on four themes; Collectif capabilities select corresponding contact need. Native FAQ details support touch/keyboard.
- Required contact fields reject empty input on Studio, Édition, Cinema, Atelier. All five valid local drafts create correct encoded WhatsApp destination 21696913500; no message sent. Collectif event selection propagated into draft. Email/phone alternatives remain available.
- JS syntax check passed (`node --check assets/homepages.js`). Static HTML parser checked assets, fragment links, H1 and prototype noindex across all five. Final browser error-log read returned no entries; not a substitute for a production monitoring setup.
- Full pages compared pairwise on phone/desktop, including below hero. Corrections to mobile header, Studio experience filter and Collectif grid verified.

## Evidence
`qa/static.json`, `phone.json`, `desktop.json`, `narrow.json`, `interactions.json`, `final-phone.json`, `final-desktop.json`; ten full-page JPG captures; five desktop opening captures; `qa/five-directions.jpg` visual comparison. Browser screenshots can differ from nominal viewport width by scrollbar width.

## Limits and follow-up
- Browser emulation, not physical devices or an accessibility certification. Semantic controls, visible focus, native dialog behavior, readable controls and reduced-motion CSS implemented. No automated axe/Lighthouse suite installed or claimed.
- Local performance delivery budget measured at asset level: 480px concept images approximately 33–43KB each, 900px approximately 87–127KB; image masters not requested by pages. JS/CSS are dependency-free; fonts use Google Fonts. Browser timing API was unavailable through the permitted read-only inspector, so timing/Lighthouse and field Core Web Vitals remain unmeasured. No conversion or SEO performance claims.
- Five current concepts share a consistent illustrative photography library for comparable evaluation. Replace with approved real work and verified case details before publication. Preserve the labels while concepts remain.
- Production sitemap/canonical/domain, genuine full page expansion, real audience validation and external WhatsApp app handoff are outside local Stage 1 verification. The WhatsApp draft URL is verified; actual delivery is not.
- All alternatives noindex; sitemap not expanded. No site publication or external profile work performed.

## Rebuild
Run `python website/build_homepages.py` from repository root after editing template source. Start with `python -m http.server 8000 --bind 127.0.0.1`. The current server is already running in the background.
