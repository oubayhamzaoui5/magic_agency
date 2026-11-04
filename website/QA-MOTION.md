# Magic in motion — verification, 2026-10-28

Current source: website/build_magic.py → index.html, assets/magic.css, assets/magic.js. Rebuild via `python website/build_magic.py`. Earlier alternatives rebuild separately via build_homepages.py and never overwrite the current root.

## Checked locally
- Chromium in-app browser, phone 390×844, desktop 1440×1000, actual app-width case 614×471, additional 320×740 narrow reflow. No document horizontal overflow.
- One H1, all local asset references and fragment targets resolve; all previews noindex. Root canonical and Organization/contact data retain incumbent business domain and contact. No fabricated office address, ratings, performance or experience statistics.
- Wall animation: native CSS loop, persistent accessible pause/resume, hover pause on image stage, page visibility/offscreen stopping. The work wall is decorative and duplicates work available in stable accessible controls; no moving keyboard or touch targets. Pausing verified all three tracks computed as paused; resume attribute toggles correctly. Reduced-motion CSS/JS path statically inspected; native OS preference was not changed for QA.
- Gallery counts: branding=3, campaign=1, digital=1, experience=1, all=6. All six gallery project dialogs opened at desktop; next Naya→Kora, Escape and focus return verified. Extra three fictional projects available through native horizontally scrollable rail. Arrow button moved rail from initial position into later work.
- Service tabs: visible panel changes, arrow-key selection, and event-to-contact prefill verified. Nine incumbent capabilities remain represented within three visitor-task groups.
- Empty form blocks with native required validation. Filled local test creates correct `https://wa.me/21696913500?text=...` link including selected need and entered text; no submission sent. Values preserved. Phone/email direct alternatives retained.
- First review detected focus-related internal wall cropping; fixed with overflow:clip and removed unstable moving click targets. Final viewport evidence confirms scrollTop=0, full 640px wall height at 1440px, loaded active images and no overflow. Five prior alternatives preserved at /directions/studio/, /edition/, /cinema/, /atelier/, /collectif/.

## Performance delivery changes
- Removed Google Fonts network dependency from current root: self-hosted variable Manrope and italic Fraunces subsets, font-display:swap, preload Latin display/body resources. Font licenses included.
- Original logo resized non-destructively to transparent 352×160 PNG, ~21KB.
- Nine eager wall images use responsive small sources; 480px new images ~14–38KB, existing ~33–43KB. Below-fold images lazy; dimensions reserved. PNG masters never referenced by pages.
- HTML + CSS + JS + logo + Latin fonts + all nine 480px eager images: static estimate 456575 bytes before transport compression, excluding later responsive upgrades/lazy requests. Full performance timing, Lighthouse and field Web Vitals are not measured. No runtime framework, animation library, video or WebGL dependency.
- No unthrottled scroll handlers, scroll hijacking, artificial loaders or hidden-before-JS page sections. State transitions use small native CSS/WAAPI operations; the continuous loop animates transforms.

## Evidence and limits
qa-motion/interactions.json, layout.json, final-layout.json, static.json and final desktop/mobile/user-width JPG captures. Detector invoked once, regex fallback because htmlparser2/css-tree/etc unavailable; zero findings is a limited static result. JS syntax and fragment/file checks pass.

Emulation and expert inspection, not participant conversion research, physical-device performance or accessibility certification. Public release still needs genuine portfolio evidence and final production indexing/domain checks. No deployment requested or performed. No completed conversion gain or design award claimed.

Independent finish review: **ship the local homepage revision**; no implementation fixes owed. One capture finding (sticky header in mobile full-page hero) was corrected and independently scored **resolved**. Native full-page capture failed at the long mobile page; mobile-final.jpg was assembled from 19 overlapping live viewport captures with recorded scroll positions in mobile-tiles.json, excluding repeated sticky chrome. The clean mobile-opening-final.jpg remains an unstitched viewport capture. No broader conversion, field-performance or accessibility certification inferred from this review.
