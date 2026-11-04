# State

## Production deployed — 2026-11-04
- User authorized pushing Git and replacing the Magic VPS site. Connected as ubuntu@51.68.124.47, ran sudo -i as the first remote command, then read /root/CLAUDE.md before inspecting the app. Production frontend commit4a73bf55877f7057193e9dccba074ba1a86f18f8 is live at https://magicbrandingco.com/.
- Repository remains /root/magic_agency, clean main checkout; root PM2 app magic_agency now serves its public allowlist on127.0.0.1:3000 through unchanged nginx TLS. Public links point to approved versioned static entry points, keeping dashboard pull/restart functional. Explicit homepage/archive index rewrites fix directory routing; unknown/private routes404. No new firewall rule, public admin backend, nginx vhost change or unrelated process restart.
- Rollback: /root/magic-deploy-backups/20261104-39343f7/ contains previous-site directory/archive, original PM2 definition, nginx/rules backups and verification records. /root/magic-runtime/rollback-be38a82.sh atomically restores the previous directory and process configuration. Runtime config: /root/magic-runtime/ecosystem.config.json.
-265 staged file hashes and HTTP responses, homepage and all archive directory URLs passed. External HTTPS/TLS check passed, live indexSHA25681e17a3438645c9b6a9301c4b2e11a7f6678c8919e529255b029c9027786f261 matches server;57 referenced assets loaded externally. Git/source/admin/directory listing paths404; encoded traversal blocked400. Magic error log empty; unrelated root PM2 PIDs/statuses unchanged. Live1440/390px layout, all eight enquiry selections, WhatsApp draft preparation without sending, and gallery passed with no console errors. Evidence: output/deploy-preview/.
- Large first Git uploads timed out; delivery objects were transferred in small temporary branches, the identical tree verified through GitHub Git API, then main advanced without force. Temporary remote branches removed. Large source PNG masters stay in the local assets folders and codex/full-source-local-backup snapshot; optimized runtime images and all build code/prompts are in Git. A clean Git export rebuilds successfully without masters.
- Production canonical/OpenGraph/structured URLs and sitemap use magicbrandingco.com. Homepage is indexable; archived proposals retain noindex and robots exclusion. Local-only image-editor link is hidden/removed on production. Local preview server restarted for persistent builder behavior.

## Editorial solutions applied to original homepage — 2026-11-04
- User explicitly selected L’éditorial solutions and requested all accepted work in the original index website with functional verification. Main /index.html now includes the accepted twelve-service editorial section followed by exactly one sage editorial solutions section, before agency. No comparison overlays on root. Header/footer add Nos solutions anchors.
- Refactored solution_variants.py to expose shared section rendering and application; build_magic.py inserts the selected section and three corresponding contact options before writing root. Alternative solution previews build from the clean base, avoiding duplicate sections/options. Source rebuild reproduced index.html byte-for-byte. Preview server restarted to retain changes during future admin hero saves.
- Browser320/390/768/1280/1440/1900px: no page overflow or overflowing headings; all twelve services retained, correct services/solutions/agency order. Desktop and mobile root screenshots inspected. All twelve service images loaded; no page errors.
- All eight need-preselection links passed. Whitespace-only form entries rejected; local test values generated the correctly encoded WhatsApp draft; editing invalidated the stale draft. No message sent and no external draft opened. Four gallery concepts, album image selection, next concept, Escape and focus restoration passed. Hero pause/resume/restoration, FAQ open/close, mobile menu open, new solution navigation/auto-close and Escape/focus restoration passed.
- Static checks: unique IDs/options, valid internal anchors, matching contact choices, no duplicate solutions/CSS.194 HTTP resources returned200, including image srcsets, gallery albums and font references. Python compilation and JS syntax pass. Detector ran once in degraded regex mode, no findings; old unrelated comp-round metadata unchanged. Evidence: qa-homepage-final/results.json, static.json and screenshots. Local original website updated; no deployment requested.

## Three solutions-section proposals — 2026-11-04
- User requested a solutions section directly under services, covering custom business platforms, automations and applications, with three variants. Built /directions/solutions-atelier/#solutions, /directions/solutions-editorial/#solutions and /directions/solutions-connexions/#solutions. Root remains available pending selection.
- Atelier uses a forest surface, featured platform and paired automation/app examples. Editorial uses three alternating open spreads on sage. Connexions connects business frictions to tailored solutions on ivory. Existing Outfit/DM Sans/Lime Studio and shared gutters preserved. All previews retain accepted12-service section immediately above.
- Native HTML/CSS interface illustrations show client portal, form-to-follow-up workflow and booking app; no bitmap weight or new runtime dependency. All marked as illustrations with accessible labels. No live business data, metrics, external integrations or fabricated client proof.
- Three solution-specific CTA choices added to preview forms and work with existing data-service-need handler. Comparison uses full-page links. No external message or deployment.
- Browser320/390/768/1440px: no horizontal overflow/heading overflow, three demos per variant, twelve services preserved; all three contact selections work and no console errors. Desktop/mobile captures and results: qa-solutions/. Unique IDs, local references/anchors, Python syntax pass. Detector ran once, degraded regex mode, no findings; unrelated old comp metadata unchanged.
- Sources and durable brief: solution_variants.py, assets/solution-variants.css, SOLUTION-SECTION-OPTIONS.json. build_magic.py regenerates previews; local server restarted for subsequent editor rebuilds.

## Editorial selected, twelve illustrated services — 2026-11-04
- User selected L’éditorial and requested each category’s individual services have their own text and image, with bold hero-like art direction and optimized files. Applied the selected composition to both / and /directions/services-editorial/; comparison bar removed from the chosen preview. Previous alternatives retained.
- Four category headers preserve the selected icons. Each now introduces three always-visible image/text features: positioning, messages/voice, communication plan; identity, packaging/edition, art direction; web/e-commerce, social, photo/video/motion; scenography, launches/activations, invitations/signage. Twelve distinct images; original approved Muse event retained for launches.
- Eleven new built-in ImageGen assets under assets/services/. Exact prompts, master/source paths, dimensions and export sizes: SERVICE-EDITORIAL-ASSETS.json. Strategy concepts use forest/lime/cobalt; VELA illustrates branding; ONDA illustrates digital; MUSE extends events. All are labelled fictional/generated. No real case claims added.
- Responsive 480/800/1200px WebP exports preserve complete 3:2 compositions. Eleven 480px exports total251512bytes; 800px total561252bytes. Lazy loading, decoding=async and reserved aspect ratios used. Images are neither cropped nor upscaled in their intended CSS display sizes.
- Sources: editorial_services.py and assets/service-editorial.css, integrated in build_magic.py for persistent hero-editor rebuilds. Existing JS service contact preselection retained.
- Browser verification320/390/768/1440/1900px: no horizontal overflow or overflowing headings, four groups/twelve features, no service tabs. Digital contact link selects the correct form need, no page errors. Desktop categories and phone digital screenshots reviewed. Static IDs/assets/anchors, 3:2 exports, Python compilation and JS syntax pass. Evidence: qa-services-expanded/. Mechanical detector ran once in degraded regex mode with no findings; unrelated stale comp metadata unchanged. Local only; no deployment or message sent.

## Three service-section proposals — 2026-11-03
- User rejected the tab layout and service photographs except Muse events; retained all four current icons and requested three variants matching newer preceding sections.
- Built full-homepage local previews at /directions/services-editorial/#services, /directions/services-panorama/#services and /directions/services-parcours/#services. Editorial uses open rows; Panorama uses asymmetric lime/ivory/forest fields and an event spread; Le fil de la marque uses a forest background and a connected service sequence. All services remain visible, with no tab/tabpanel roles. Each section uses only the retained events photograph and four selected icons.
- Current homepage service composition stays available pending selection. Other homepage sections retain their markup. Comparison footer links navigate separate pages. Service contact links preselect the existing form need without sending anything.
- Sources: service_variants.py, assets/service-variants.css, SERVICE-SECTION-OPTIONS.json. Main builder regenerates all previews on future hero saves; preview server restarted. Shared JS now safely handles pages without tabs.
- Browser checks at1440/390/320px: no horizontal overflow, four services and zero tabs per proposal, all four icons loaded; correct digital contact preselection and no page errors. Phone panorama text widened after initial inspection. Local assets, anchors, unique IDs, Python compilation and JS syntax pass. Evidence: qa-services/. Mechanical detector ran once in degraded regex mode with no findings; unrelated pre-existing comp-round metadata remains stale. No deployment or external message.

## Hero artwork expansion and aspect correction — 2026-11-01
- Replaced active hero rotation with 14 distinct original fictional-brand creatives generated using built-in ImageGen. Exact prompts, actual dimensions and provenance: HERO-CREATIVE-ASSETS.json. Workspace masters and 480/900/1400 WebP assets: assets/hero/. Previous saved selection backed up at content/hero-before-portrait-20261101.json.
- Tile proportions now follow actual artwork: mainly .68/.907 width-to-height plus one square. Desktop three columns, mobile two 200px-high rows with variable widths; contain prevents artwork cropping within each tile. Existing reference geometry, 16px gaps, Magic branding/copy and motion control retained.
- Hero-only editor exposes all 14 new assets, complete-image previews and native-aspect uploads. Derivative resize bounds height to4096px and reports actual srcset widths.
- Browser checks at1900/1280/390/320px: no horizontal overflow, 14 unique images, all hero images loaded, native proportions retained. Phone hero remains836px high. Editor shows14 selections in3 columns; reorder then undo restores MIRO first. API verifies authentication, save/rebuild, stale-revision rejection and portrait upload proportions; temporary upload files removed.
- Evidence: qa-clarity/hero-artwork-desktop.png, hero-artwork-mobile.png, hero-artwork-reflow.json, hero-artwork-api.json. Syntax/compile checks pass. One detector pass in degraded regex mode reports only existing12/28px admin typography advisories; no full accessibility certification. Unrelated stale comp-round metadata left unchanged. No deployment or external message.

## Live Superside hero geometry — 2026-11-01
- Latest user request supersedes earlier approximate hero and tilted landscape image framing: match live Superside desktop/mobile spacing, sizing and image side with Magic identity/copy/artwork. Measured rendered DOM at 390/768/1024/1280/1440/1900px, including responsive CSS rules.
- Implemented reference breakpoints 768/1280/1650, container widths 1216/1608, fixed transparent 56/78px header, 160px desktop vertical padding, typography36/44,60/72,72/80,88/88, 532px supporting paragraph and 52px pill CTA. Three desktop portrait columns with16px gaps; mobile two edge-to-edge horizontal rows of140x200px tiles. Reference alpha fades, no blur. Magic logo, palette, fonts, slogan and images retained.
- Hero editor migrated two existing columns without losing selections/order and adds a third column. All three remain editable with destination-specific move buttons; mobile rows derive from same saved imagery. Authenticated save/rebuild and revision checks pass. Removed sections stay removed.
- Browser evidence: qa-clarity/hero-reference-desktop.png (1280px), hero-reference-wide.png (1900px), hero-reference-mobile.png (390px), hero-reference-metrics.json. At390px headingy80, CTAy304, wally380 and heroheight836 exactly match live reference. At1900px containerx146/width1608 and wallx1096/width804 match; Magic font metrics cause subpixel text-height differences.
- Detector run once: existing admin12/28px type advisories; incidental old comp-round metadata remains unrelated to this implementation-directed request.

## Hero slogan and CTA composition — 2026-11-01
- User supplied a Superside screenshot as the exact text/CTA layout reference and requested the slogan « De l’idée à l’impact. », retaining Magic branding.
- Hero now uses that slogan on two lines, cream Manrope and gold italic Fraunces; existing supporting French paragraph; one text-only gold project CTA below. Removed hero expertise links, secondary CTA, sparkle and signature. Existing header controls, campaign imagery, motion control and saved image choices retained.
- Desktop hero/header alignment uses a 1480px maximum container. Copy is vertically centered with reference-like spacing; image wall still clips sharply at section edges with complete side framing. Mobile keeps the same reading order above the wall.
- Checked 320/390/760/1000/1440/1900px: no horizontal overflow; heading, paragraph and CTA align left; exactly one hero-copy link; CTA reaches #contact. Detector ran once in degraded regex mode, no findings. Evidence: qa-clarity/hero-impact-desktop.png and hero-impact-mobile.png. Local server restarted so subsequent hero-editor saves retain the new markup.

## Service icon revision — 2026-11-01
- User explicitly accepted only the generated strategy compass and rejected the first branding/digital/events icons. Compass original and web assets remain unchanged.
- Three new built-in ImageGen assets now replace those rejected icons: branding swatch fan, digital globe with cursor, event ticket. Same green enamel, ivory and brass treatment; transparent PNG originals and 144/288px web versions retained in assets/service-icons/. These replacements await user feedback; do not describe them as approved.
- Exact prompts, sources and saved paths: SERVICE-ICON-ASSETS-V2.json. First set: SERVICE-ICON-ASSETS.json. Builder selects the compass plus the three v2 filenames; server restarted so hero-editor saves preserve them.
- Desktop 1440px and mobile 390px: all four icons load, no page/tab overflow. Tab behavior had already passed pointer and keyboard checks with the same markup structure. Strategy original hash matches its generated source. Detector ran once in degraded regex mode, no findings; not a full audit. Evidence: qa-clarity/service-icons-v2-desktop.png and service-icons-v2-mobile.png.

## Hero editor — 2026-10-29
- User requested smaller gaps and a password-protected image/order interface. Hero gaps reduced to 18px vertically and 18px/20px between columns; full side edges preserved.
- Local /admin/ editor supports library selection, uploads, labels, add/remove, drag reorder, keyboard/touch arrows and cross-column movement. Explicit save rebuilds public HTML; JSON persists selections. Server enforces password sessions; verifier stored outside served root. See ADMIN.md.
- Current image choices/order restored after verification. User confirmed hero-only editor; portfolio albums unchanged.

## Hero framing refinement — 2026-10-29
- User requested complete left/right image edges, sharp top/bottom cuts at the hero boundary, no fade and an icon-only white circular play/pause control.
- Tilt now belongs to each tile, with horizontal clearance. Desktop image wall stretches to the hero's top and bottom; mobile wall finishes at the section bottom. Stage mask and arrival clipping removed. Hero disclosure removed as requested; portfolio concept disclosures remain.
- Builder, generated homepage, CSS and motion handler updated together. Five widths (320/390/760/1440/1892px) verified: no side clipping or horizontal overflow, all hero images loaded, pause/resume and reduced motion work, no page errors observed. Evidence: qa-clarity/hero-framing.json and hero-framing-*.png. Mechanical scan ran once in degraded regex mode, no findings; not a full accessibility audit.

- Stage: 1 — main homepage deeply redesigned, verified locally and independently reviewed. Earlier five directions archived and still reviewable.
- User authorized local redesign prototypes and mockup imagery, five variants; no deployment.
- Existing index is tracked by Git; original asset files preserved.
- User feedback: previous result felt off; asked for Superside-like personality and movement, deep modification, richer generated imagery, UI/UX and conversion quality. Explicitly selected “Playful, bold and art-directed” on 2026-10-28. This authorizes one focused root revision; no new five-way tournament needed.
- Acceptance: user explicitly likes the current direction and requests a more human, less generic refinement with more imagery and personalized icons. Existing visual world accepted as the starting point; no award or conversion performance claims.
- Next: user feedback on the 2026-10-29 clarity and brand-image expansion. Stage 2 pages remain planned, not built.
- Current preview: /. Archive routes: /directions/studio/, /directions/edition/, /directions/cinema/, /directions/atelier/, /directions/collectif/. Root has a quiet footer archive disclosure; the fixed comparison bar is removed from the current design.
- Current root: Magic in motion — living campaign wall, varied conceptual work, grouped service selection and simplified enquiry. Earlier Studio 360 now /directions/studio/. Archive builder and current-root builder are independent.
- QA: 320px/390px/1440px no horizontal overflow across all five; all concept images loaded; every gallery detail opened, Escape and focus return verified; mobile menus, filters, disclosures/capability preselection and contact draft preparation tested. Static asset/anchor/indexability checks passed. Evidence: qa/ and QA.md.
- No external message sent, no deployment, no production indexing changes. Every prototype uses noindex and alternatives are absent from sitemap.
- Production dependencies: selected direction; genuine project imagery and case descriptions; owner confirmation of partner usage and geographic scope; real published SEO and external contact handoff checks. No testimonial evidence available.

## Current revision evidence
- Direction contract: MOTION-DIRECTION.md; exact prompts/source paths: MOTION-ASSETS.json; QA evidence: qa-motion/.
- Five additional built-in generated assets copied under assets/magic/ with 480/900/1400 WebP variants. Original logo optimized without recoloring. Manrope/Fraunces Latin and Latin-ext WOFF2 self-hosted with OFL license files.
- Static first-party initial asset estimate: 456575 bytes (all nine eager 480px wall photographs, Latin fonts, HTML/CSS/JS and logo), not measured LCP/INP or production transfer.
- Browser checks: 320/390/614/1440px no horizontal overflow. All active desktop images loaded. Pause/resume, category counts, native dialog next/Escape/focus return, service tabs/arrow keys, service-to-brief prefill, empty-form validation and correct encoded WhatsApp draft passed. No actual message sent.
- Material first-review fix: moving wall used overflow:hidden, allowing focus-related internal scrolling/cropping. Changed to overflow:clip and made motion wall decorative, retaining stable accessible gallery controls. Pause no longer competes with control focus/hover. Final wall scrollTop=0 and full 640px desktop window verified.
- Skill tooling note: Impeccable concept seed considered; user-pinned direction carried through. Build delivered as an implementation-direct revision under explicit task authorization. No design comp was approved; incidental .impeccable comp-round metadata is not evidence of an approved comp or the current artifact's completion status. Static detector ran once in degraded regex mode, no findings; not accessibility certification.
- Independent finish review: ship local homepage revision, no implementation fixes owed. One mobile full-page capture artifact corrected; reviewer explicitly scored it resolved. Long mobile capture assembled from 19 overlapping viewport screenshots after native full-page capture failed, with recorded scroll offsets and repeated sticky chrome excluded. Clean desktop and phone opening screenshots retained.

## Human-polish refinement
- Keep accepted composition, motion, palette, logo, existing work and contact paths. Four new images (Pulse, Grain, Palma, illustrated creative table) in assets/magic/; exact prompts/provenance in HUMAN-ASSETS.json. New mockups extend the same approved art direction; generated process scene visibly labelled.
- Original 18-icon SVG family (eight brand symbols, ten controls), 32px frame / 1.6 stroke / Magic sparkle and palette. Source: magic_icons.py, sprite: assets/magic-icons.svg, reusable vectors: assets/icons/, preview: /website/icon-preview.html. Services/process use meaningful custom symbols rather than generic icon-pack pictograms.
- Warmer French copy, three art-direction notes and a tactile image pairing give the page authored detail. Scope and claims preserved. No fake people, testimonials or result metrics.
- Enquiry now rejects whitespace-only entries and removes stale draft links after edits; updated draft regenerated correctly. All values retained, no auto-send.
- Local QA at 1440/390px plus reflow at 320/614px: no overflow; custom sprite icons visibly render; pause/resume icon swapping, service arrow keys, all three new project images, phone draft, whitespace validation and edited-draft regeneration verified. Evidence: qa-human/ and HUMAN-POLISH.md. Detector: one degraded regex scan, no findings; not a full audit.

## Clarity and brand-image expansion — 2026-10-29
- User asked to preserve accepted aesthetic, explain strategy/branding/web/social/events, show concrete examples and add more images. Latest steering explicitly retires Zéra, Rencontres, Soli and the gold ornament from the active page, and authorizes multiple images per retained brand.
- Nine new selected generated assets: Grain strategy workshop, Palma digital rollout, Muse event, Naya hands, Naya campaign, Kora campaign, Pulse lifestyle, Saison campaign, Palma campaign. Exact built-in prompts/references/source paths: CLARITY-ASSETS.json and BRAND-EXPANSION-ASSETS.json.
- Seven main brand families, sixteen visible campaign images, two or three images per family. Secondary views open directly in their album; thumbnail and keyboard image switching, previous/next brand and focus return work. Rejected images absent from root and project JSON; original source files/archives preserved.
- Four explicit expertise tabs moved before examples. Each has an example and concrete deliverables. Hero links activate matching expertise; service-to-form preselection uses explicit values.
- All reading-gallery, service and dialog images retain their complete 3:2 framing. Hero has two landscape lanes and no overlay seal. Removed mobile floating contact bar to keep images unobstructed; header contact remains.
- Verification: QA-CLARITY.md and qa-clarity/. Five-width reflow passed, zero browser console entries observed, all local image/anchor references exist. Service keyboard, gallery/filter/album and WhatsApp draft preparation/edit invalidation passed. No external message or deployment.

## Section removal — 2026-10-30
- User requested removal of the main portfolio section and three-step process section. Removed both from builder and generated homepage. Existing examples navigation now targets the retained exploration rail. Dialog project navigation derives its order from remaining project buttons. Local server restarted to preserve removal on future editor saves. Internal anchors and JavaScript syntax verified.
## Hero brand replacements — 2026-11-03
- User rejected FABLE illustration and ALTO phone campaign in the hero and requested new brands matching the other images.
- Built-in ImageGen created KOVA specialty coffee (cobalt/yellow packaging) and VELA fragrance (amber/apricot still life). Both are fictional concepts awaiting user feedback.
- Masters and 480/900/1400px WebP variants saved in assets/hero/. Full prompts and source paths: HERO-REPLACEMENT-ASSETS.json.
- Persisted hero selection and fallback defaults replace ALTO with KOVA and FABLE with VELA in the same positions. Rebuilt index.html; other selections preserved.
- Checked both desktop/mobile renderers, saved selection validation, served homepage and all six new asset URLs. Existing rejected source files remain available in the library.

## Bold static hero — 2026-11-03
- User requested bolder poster-like styling for the left hero while preserving its wording and button, with no animation.
- Hero headline now uses uppercase Manrope 800 on both lines, cream/gold, upright lettering, tight leading, responsive 32–96px sizing. Supporting copy gains modest weight; button label, shape and contact target retained.
- Hero animation/transition disabled, campaign tracks use fixed composed offsets, pause control and its JS lifecycle removed. Other sections retain existing behavior.
- Browser QA at 320/390/768/1280/1900px: no horizontal overflow, full headline fit, all hero images load, zero hero animations, no pause control and no page errors. Screenshots: qa-clarity/hero-poster-1900.png and hero-poster-390.png. Detector returned no findings with stale comp-round metadata; this scoped user-directed refinement does not reopen the prior direction exercise.

## Hero spacing, restored image motion and WhatsApp — 2026-11-03
- User clarified only left content should be static; right images must keep animation. Restored campaign-track animation, pause/resume and offscreen suspension; reduced motion still disables animation.
- Added 8px between headline lines; paragraph gap reduced to 16px mobile/20px desktop; button gap reduced to 20px.
- Added green WhatsApp button with white brand icon/text, linking to existing agency number at https://wa.me/21696913500. Existing hero CTA now white text on deeper gold to preserve readability. Original wording and contact anchor unchanged.
- Browser checked 320/390/768/1280/1900px: no overflow, headline fits, all images load, left copy has zero animations while visible tracks move, pause works, reduced motion has zero hero animations, both buttons have white text and correct targets, no page errors. Screenshots and metrics: qa-clarity/hero-whatsapp-1900.png, hero-whatsapp-390.png and hero-whatsapp.json. No external message sent.


## Lime Studio palette and font proposals — 2026-11-03
- User selected palette 1, Lime Studio. Applied forest #102F29, original logo green #0B6959, ivory #F5F8EE, lime #D8F36A and sage #E2EAD7 throughout homepage tokens, overlays, focus accents, navigation and form. Hero CTA uses logo green with white text; WhatsApp keeps its existing green. Original imagery and fonts retained.
- Selected palette recorded in PALETTE-OPTIONS.json; builder theme-color and design/product context updated. Local preview server restarted to load builder update.
- Desktop/mobile at 1440/390/320px: no horizontal overflow, hero images loaded, mobile menu and service tabs function. Relevant computed text contrast ratios range from 5.23:1 to 13.38:1. Detector returned no findings and reported existing stale comp-round metadata. Evidence: qa-palette/.
- Five font proposals saved in FONT-OPTIONS.json; comparison uses selected Lime Studio and actual French copy. Families load from Google Fonts in comparison only. Live homepage keeps Manrope/Fraunces pending user selection.

## Outfit + DM Sans applied — 2026-11-03
- User selected option outfit from additional font previews. Outfit 800 now drives h1/h2/h3 and upright colored emphasis; DM Sans 400–700 drives body, navigation, buttons and form. Lime Studio palette retained.
- Self-hosted Latin/Latin Extended variable WOFF2 assets and OFL license files added. Font CSS replaces old families; builder preloads selected Latin files and cache-versions font CSS. Local server restarted for persistent editor rebuilds.
- Read-only independent typographic assessment found no layout adjustment needed across five widths. Mechanical type scan returned no findings, with existing stale comp-round metadata.
- Actual local-font browser checks at 320/390/768/1280/1900px: all font faces load, French accents/ligatures checked, hero and visible section headings fit, no page overflow/errors, service tabs work. Evidence: qa-font/results.json and screenshots.

## Shared section gutters — 2026-11-03
- User requested all section left/right spacing match hero copy, with hero right artwork excepted. Shared container now derives width/gutters from hero tokens; exploration rail uses same bounded width and zero extra inline padding/scroll padding. Header centers at ultrawide sizes.
- Before: at1440px hero left112px but sections48px; at1900px hero146px but sections270px. All section containers/header/rail now match hero left/right edges. Hero artwork bounds unchanged.
- Checked320/390/614/768/1280/1440/1900/2560px: every section edge matches within1px, symmetric page insets, no horizontal overflow, visible headings fit, gallery arrows still scroll. Desktop/phone screenshots reviewed. Layout detector returned no findings with existing stale comp metadata. Evidence: qa-spacing/before.json, results.json and screenshots.

## Rubans signature partners applied — 2026-11-03
- User selected Rubans signature, with all12 original partners from PARTNER-OPTIONS.json. Replaced six-logo strip with centered heading and two opposing monochrome logo ribbons, lateral fades, French pause/resume control and shared hero-aligned container. Outfit/DM Sans and Lime Studio retained.
- Builder reads full partner manifest, making all12 accessible names available once; decorative duplicates have empty alt and aria-hidden groups. Original assets retained; trimmed/scaled lossless WebP derivatives total409776bytes.
- Motion pauses offscreen/when tab hidden and stores independent session pause preference. When section enters view, all partner assets preload to avoid blank marks later in the loop. Reduced motion and no-JavaScript use static grids with all12 partners. Local server restarted to preserve selected section on editor rebuilds.
- Browser checks at320/390/768/1280/1900/2560px: all logos load, row groups span their viewport, matching section edges, no horizontal overflow/errors, pause/resume works, reduced-motion has no animation and all originals visible. No-JavaScript has12 partner names. Desktop/mobile and reduced-motion screenshots reviewed. Evidence: qa-partners/. Mechanical detector returned no findings with existing stale comp metadata.

## Partner pause control removed — 2026-11-03
- User requested removing partner pause/resume button. Removed markup, control styling, click handler and saved partner pause preference. Logo animation, automatic offscreen/tab suspension, asset loading and reduced-motion/static fallback retained.
- Rebuilt homepage and restarted local server for persistent editor rebuilds. JavaScript syntax and browser checks at390/1900px passed: zero partner buttons, all12 partner names, running logo rows, no overflow/errors, reduced-motion disables animation. Hero control unchanged.

## Partner logo adjustments — 2026-11-03
- User requested slightly larger Pharmacie Centrale logo and frameless SPAUZ. Increased Pharmacie width about28%; CSS clips SPAUZ outer frame at original aspect ratio. Source assets retained.
- Rebuilt and restarted local preview. Desktop1900/mobile390 screenshots reviewed; correct logo dimensions/clip, no horizontal overflow. Both ribbon copies and reduced-motion fallback share per-partner selectors. Evidence: qa-partners/pharmacie-centrale-tunisie-*.png and spauz-*.png.

## New Magic section image concepts — 2026-11-03
- User requested a new section immediately below partners with reference text-left/square-image-right composition, about Magic and problems it solves. Five distinct built-in ImageGen concepts generated, inspected and saved under assets/magic-about/. No live section inserted before user image choice.
- Concepts: Le fil conducteur, Sortir du cadre, Tout se répond, Faire entendre sa marque, Une idée partout. All square, forest/lime editorial direction. Exact prompts, original source paths, saved assets and draft French copy in ABOUT-SECTION-OPTIONS.json.
- Draft proposition: turn scattered ideas and inconsistent brand touchpoints into one clear recognizable identity, through Magic strategy/branding/digital/experiences. No fabricated performance claims. Generated people/scenes are illustrative, not actual Magic staff.
