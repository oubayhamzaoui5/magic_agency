---
name: Magic 360 — Magic in motion
description: Bold static hero copy beside an animated campaign wall within the selected Lime Studio palette.
heroPosterRevision: "2026-11-03 latest user-directed refinement: preserve headline wording and supporting copy; heavy upright uppercase Outfit 800 on both headline lines, pale ivory/lime, line-height .98, tracking -.04em, responsive 32–96px, 8px gap above second line. Paragraph top gap 16px mobile/20px desktop, buttons top gap 20px. Left copy has no animation; right campaign wall restores continuous motion, pause/resume, visibility suspension and reduced-motion support. Original contact CTA retains wording/target with white text on logo green; adjacent green WhatsApp button has white brand icon and label, links to existing +21696913500. Other sections preserve existing styling and behavior. KOVA and VELA product campaigns replace ALTO and FABLE in persisted hero selection."
heroCopyContract: "2026-11-01 exact live Superside geometry: breakpoints 768/1280/1650px; container viewport minus 32px mobile, minus 64px tablet, 1216px desktop and 1608px wide; fixed transparent header 56/78px; mobile heading36/44 at y80, body16/24 margin16, CTA52 full width margin24, two horizontal image rows 200px high, width derived from native aspect ratio, gap16; desktop padding160, copy50% with header-height top padding, heading72/80 or88/88, paragraph532px at18/26 margin24, CTA52 margin40, right-side three portrait columns gap16 (ratios .9067/.68), section min-height656 or965. Magic wording De l’idée / à l’impact., existing supporting copy, Outfit/DM Sans, pale ivory/lime/forest; 14 original fictional-brand creatives, upright at native aspect ratios with contain framing. Live reference alpha fades replace earlier sharp framing under latest exact-match request; no image blur. Editor manages three columns, mapped in saved order into two mobile rows; uploads and previews preserve native proportions."
colors:
  forest: "#102F29"
  green: "#0B6959"
  teal: "#0B6959"
  cream: "#F5F8EE"
  paper: "#F5F8EE"
  mint: "#E2EAD7"
  butter: "#D8F36A"
  muted: "#436052"
  line: "rgba(16,47,41,.18)"
typography:
  display:
    fontFamily: "Outfit, sans-serif"
    fontSize: "clamp(43px,5.2vw,76px)"
    fontWeight: 800
    lineHeight: 1.06
    letterSpacing: "-.04em"
  headline:
    fontFamily: "Outfit, sans-serif"
    fontSize: "clamp(34px,4.1vw,56px)"
    fontWeight: 800
    lineHeight: 1.09
    letterSpacing: "-.04em"
  accent:
    fontFamily: "Outfit, sans-serif"
    fontWeight: 800
    letterSpacing: "-.035em"
  title:
    fontFamily: "Outfit, sans-serif"
    fontSize: "24px"
    fontWeight: 800
    lineHeight: 1.25
    letterSpacing: "-.03em"
  body:
    fontFamily: "DM Sans, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.7
  action:
    fontFamily: "DM Sans, sans-serif"
    fontSize: "13px"
    fontWeight: 700
    lineHeight: 1.4
rounded:
  image: "12px"
  logo-chip: "5px"
  pill: "30px"
  primary-action: "40px"
  circle: "50%"
spacing:
  gutter: "20px"
  gutter-medium: "32px"
  gutter-wide: "48px"
  section: "64px"
  section-wide: "90px"
components:
  button-primary:
    backgroundColor: "{colors.butter}"
    textColor: "{colors.forest}"
    rounded: "{rounded.primary-action}"
    padding: "9px 10px 9px 23px"
    height: "52px"
    typography: "{typography.action}"
  button-primary-hover:
    backgroundColor: "{colors.cream}"
  button-submit:
    backgroundColor: "{colors.forest}"
    textColor: "{colors.cream}"
    rounded: "{rounded.primary-action}"
  button-submit-hover:
    backgroundColor: "{colors.teal}"
  filter:
    rounded: "{rounded.pill}"
    padding: "10px 15px"
    height: "44px"
  filter-selected:
    backgroundColor: "{colors.forest}"
    textColor: "{colors.cream}"
  brief-panel:
    backgroundColor: "{colors.cream}"
    textColor: "{colors.forest}"
    rounded: "{rounded.image}"
    padding: "27px"
---

# Design System: Magic 360 — Magic in motion

## Overview

**Creative North Star: "The living campaign wall"**

Magic is playful, bold and art-directed: a forest-green stage holds clear ivory type, lime emphasis and a deliberately varied collection of creative imagery. A stable message and enquiry path sit alongside expressive photography. Movement gives the work a pulse while reading and decision controls remain still.

The original wizard logo, French language and recognizable green/pale ivory/lime identity remain the visual anchors. Portfolio imagery supplies lavender, cobalt, red and orange without turning those campaign colors into interface tokens. Superside informs personality, movement and craft; it does not supply Magic's identity, business model or customer evidence.

**Key Characteristics:**
- Stable language and contact controls beside a decorative moving wall.
- Mixed image scale, offset editorial grids and one material 3D sparkle composition.
- Sans-serif clarity with italic serif warmth; rounded imagery and pill actions.
- Visible fictional-concept disclosure, separate from incumbent partner assets.
- Native controls, local fonts, responsive imagery and user-controlled motion.

### Authority, scope and evidence

This is the authoritative record for the current root homepage, refreshed on 2026-10-28 after the independent reviewer disposition **“ship local homepage revision; no implementation fixes owed.”** That is a local finish-review judgment, not user acceptance, a deployment, an award or measured conversion evidence. The earlier research and five prototype systems are preserved below as history; their old measurements are not current root requirements.

Built source truth: [root HTML](../index.html), [current CSS](../assets/magic.css), [current JS](../assets/magic.js), [font declarations](../assets/fonts/magic-fonts.css). [build_magic.py](build_magic.py) generates the root HTML; current CSS/JS are separate source files. [PRODUCT.md](../PRODUCT.md) owns business truth; [MOTION-DIRECTION.md](MOTION-DIRECTION.md) records intent; [QA-MOTION.md](QA-MOTION.md) and [qa-motion/](qa-motion/) record the completed verification. The adjacent [.impeccable/design.json](.impeccable/design.json) extends this document with motion, breakpoints, shadows and component previews; it is not a second token authority. Do not create a competing root DESIGN.md.

The frontmatter extracts reused built values. Component `height` entries represent CSS **minimum** heights; CSS remains definitive for responsive overrides. The stylesheet also declares `--gold` and `--ink`, but current selectors do not consume them; do not infer new interface roles from unused declarations. Exact color primitives live above; the prose names their roles. The sidecar's eight-step OKLCH ramps are synthesized same-hue/chroma preview strips, not colors used by the page or new production tokens; its snippets are isolated visual previews of the cited built components, not a second interactive implementation.

Existing QA verified Chromium reflow at 320×740, 390×844, 614×471 and 1440×1000 with no document horizontal overflow; pause/resume, filters, dialogs, service selection and draft generation were exercised. Reduced-motion behavior was inspected in source; the native OS preference was not changed. No fresh QA loop was run for this documentation pass. Physical-device performance, field Web Vitals, participant research, production indexing and accessibility certification remain unverified. The static initial asset estimate in QA is not a measured load time.

### Archived research and five prototype systems

The following original record is retained for traceability. `/` is now **Magic in motion**. Studio 360 lives at `/directions/studio/`; the other archives are `/directions/edition/`, `/directions/cinema/`, `/directions/atelier/` and `/directions/collectif/`. Their builder, `build_homepages.py`, is independent of the current-root builder. The original Studio recommendation was not a user selection. Prototype-only spacing, composition and comparison navigation below do not override the current system.

#### Original research, 2026-10-28

- https://www.superside.com/ — inspected rendered desktop, source and navigation. Adopt portfolio close to first action, mixed image scale, clear service browsing and contextual contact. Adapt dark creative-studio feel to Magic's verified greens/pale ivory/lime. Reject copying subscription model, customer claims, text or lime palette. Aesthetic reference, not measured Magic conversion evidence.
- https://www.doze.agency/realisations/ — inspected rendered Tunisian agency portfolio and published project labels. Adopt visual project browsing with explicit discipline labels. Reject oversized empty opening and hidden project scope. This is an observed relevant-market pattern, not causal effectiveness evidence.
- Local intent sample: French agency communication/branding Tunisia query returned THCOM, Trame, LANCI and Doze. Supports a meaningful agency homepage and service-family roadmap, not city matrices. No search volume, controlled geo-rank or comparable outcome study established.
- https://www.nngroup.com/articles/hamburger-menus/ — primary quantitative study, 179 participants / six sites, supports visible desktop and combined mobile navigation. Transfer: keep project/action links visible and use an explicit mobile Menu for secondary paths. Study is old and cross-sector; not an agency conversion estimate.
- Phone inspection: Doze at 390px showed stacked portfolio cards and horizontal discipline filters; contact moved behind the menu. Superside browser override initially retained its previous desktop viewport, so its mobile visual journey was not verified. Do not claim Superside mobile inspection. Magic's own phone interactions were verified. Local design performance remains a hypothesis until audience testing.

#### Original direction note
Help French-speaking Tunisian decision makers judge creative scope quickly and begin a conversation. Keep Magic logo and deep green/pale ivory/lime; use actual partner assets separately from imaginary portfolio concepts. Each theme provides a phone-first visible contact action, tap-accessible project detail, service exploration and contact channels. No fabricated evidence or result figures.

#### Original five whole-page systems
| Theme | Basis / fit | Typography and palette | Whole-page composition / imagery | Signature, phone behavior | Tradeoff |
|---|---|---|---|---|---|
| Studio 360 | Superside portfolio-led browsing; broad agency | Manrope + Fraunces italics; forest dominant, pale ivory/lime | Split collage opening; asymmetrical project gallery; dark service accordion/image split; divided process; gold enquiry | Stacked photographic windows; tap project details and service disclosures | Strongest overall balance; recommended, not accepted |
| Édition | Local portfolio discipline labels + editorial visual hypothesis | Fraunces dominant; paper and green rules | Magazine masthead, cover image, numbered irregular projects, indexed service rows, vertical process and serif contact | Editorial folios, project filter; single-column phone reading | Quieter craft, less immediate campaign energy |
| Grand écran | Event/outdoor service scope; cinematic hypothesis | Bold sans, small serif accent; dark green/gold | Immersive photographic opening, widescreen project chapters, service bands, image-backed methodology and film-credit footer | Full-width image scenes and gallery detail; no autoplay | Strong event/production presence, heavier visual emphasis |
| Atelier | Packaging/brand scope; tactile art direction hypothesis | Warm serif headings, Manrope body; cream with gold/green | Centered paper composition, staggered framed work, material/service tiles, workshop steps, stationery contact | Angled paper mounts, no rotation on phone; tap details | Personal craft character, less corporate |
| Le Collectif | Wide service scope and decision routing; modular hypothesis | Sans and compact numbered labels; light green/forest | Functional grid opening, capability matrix, filterable project index, structured workflow and split brief panel | Precise quadrant grid and project filters, stacked phone modules | Clearest scanning, less editorial drama |

#### Original shared constraints
Phone gutters 20px, controls >=44px, readable 16px body. Content maximum 1280px; meaningful spacing 48–88px rather than viewport-height filler. Desktop navigation visible, phone CTA + menu. No hover-only actions. Semantic headings, native details/dialog, focus rings, Escape/focus return, reduced motion. Coherent inline SVG stroke icons. Gold uses dark-green text, never small white text. Preview switcher is outside product navigation. Five alternatives noindex, omitted from sitemap; no deployment.

Image masters 1536x1024, responsive WebP 480/900/1400. Reserve dimensions and eager load first images; lazy load lower imagery. No stock URLs or new client testimonials. Preserve established contact/anchor intents with in-page destinations.

#### Original five-variant finish review
- Observation: phone header exceeded available width. Hypothesis: logo and three control widths plus gaps exceeded the content box. Change: compact phone logo/gaps/contact padding. Evidence: 320px and 390px DOM overflow checks and screenshots. Result: no page overflow on all five.
- Observation: Studio's experience filter lacked a gallery item. Change: include the event concept as a full-width final image. Result: all categories have relevant projects.
- Observation: Collectif's auto-placement put the headline below the image. Change: explicit row/column coordinates on desktop. Evidence: final desktop opening and full-page screenshot. Result: intended title-and-image quadrant composition restored.
- Full-page pairwise phone/desktop review: Studio dark split service/photo + asymmetrical work; Édition paper folios + ruled vertical narrative; Cinema full-width scene chapters + dark credit bands; Atelier mounted paper + material tiles; Collectif capability matrix + functional image index. Common factual utilities do not impose one section shell. Native navigation and contact controls remain intentionally familiar.

## Human polish and original Magic icons

The user explicitly accepted the current direction as the starting point and requested a less generic, more human finish. This refinement preserves the visual world and interaction structure. The hero retains its headline; warmer supporting copy, three specific art-direction notes, service language based on the visitor’s starting point, and a brief reassurance provide authorship without invented claims or fake handwriting.

The icon system is now original to Magic, rather than imported from the archived prototype helper: `website/magic_icons.py` generates `assets/magic-icons.svg`, 18 editable standalone SVGs under `assets/icons/`, and the noindex `website/icon-preview.html`. Eight brand symbols (brand, voice, experience, listen, wand, launch, paper, spark) and ten functional controls use a 32×32 frame, 1.6-unit rounded stroke, curved four-point sparkle and secondary cream/mint/gold fills. SVGs inherit currentColor, --icon-accent and --icon-wash. Icons are decorative alongside names/labels; all uses are aria-hidden and controls keep textual accessible names. Service symbols are about 47px; process symbols 58px. A small service hover response stops under reduced motion. Familiar navigation semantics remain intact.

The moving wall still uses nine eager small images; Pulse, Grain and Palma add variety without increasing lane count. The extra-work rail has five items, while its native scroll/arrow controls and the six-work filter grid remain unchanged. All twelve fictional projects are available in the detail viewer. New imagery and exact prompts are recorded in HUMAN-ASSETS.json; the process photo is explicitly illustrative. Detail and form state verification lives in HUMAN-POLISH.md and qa-human/. This is local expert QA, not measured conversion evidence.

## Colors

Forest and cream establish the branded stage; pale gold supplies warmth, mint opens up service browsing, and the imagery carries the stronger campaign colors.

### Primary
- **Forest**: hero, agency, contact, default header, active filters and submit action; the principal dark text on light surfaces.
- **Teal**: italic emphasis on light surfaces, selected service text, light-surface focus outlines and interactive accents.

### Secondary
- **Butter / pale gold**: primary actions, dark-surface italic emphasis, sparkle symbols, the 360° seal and process section. Its text is forest rather than white.
- **Green**: supporting dark-green image fallback and fine process symbol/rule treatments.

### Neutral
- **Cream**: body canvas, reversed type, logo chip, form and dialog surfaces.
- **Paper**: subtly distinct partner and exploration-rail surfaces.
- **Mint**: services background, image fallbacks, secondary text on forest and draft-ready link surface.
- **Muted**: supporting copy on light backgrounds; never an instruction to mute essential controls.
- **Line**: shared transparent green divider/border; opacity lets it work across the light surfaces.

**The Stable Frame Rule.** Keep navigation, action semantics and reading surfaces in Magic's interface palette; let each clearly labelled concept own its photographic palette.

## Typography

**Display and body:** Manrope with sans-serif fallback. **Italic accent:** Fraunces with Georgia, serif fallback. No separate mono or icon font is used.

Fonts are self-hosted WOFF2 Latin/Latin-ext subsets via `assets/fonts/magic-fonts.css`, with `font-display: swap`. Manrope is normal variable weight (400–800); Fraunces is italic (400). The root preloads both Latin resources. Sources and SIL Open Font License files are retained in `assets/fonts/`; the current root makes no Google Fonts runtime request. This does not describe the archived prototypes' font loading.

The frontmatter gives base roles, not one fixed scale for every viewport. The hero is compact and tightly set, with a single italic phrase kept on one line. Base display clamp is overridden to 38px below 360px, 62px at 600–999px, `clamp(54px,5.2vw,76px)` from 1000px, and 76px from 1350px. Section headlines use the headline clamp with deliberate component overrides; agency and contact headlines are not interchangeable sizes.

Body's inherited base is 16px, while authored paragraphs use 13–16px according to context; hero copy uses a more open 1.8 line height. Global paragraph measure is at most 65ch and key intro measures are tighter (roughly 42–48ch). Titles start at 24px with a 1.25 line height; project titles grow from 23px to 29px. Small 9–12px text is used for labels and disclosures, not long reading passages. Fields remain 16px at all widths. Action weight is 700; text links use 600. Headlines balance text where declared, while the hero retains explicit line breaks.

**The Two Voices Rule.** Keep the message in Manrope and the warm emphasis in italic Fraunces. Do not replace the original logo with typeset lettering or a generated wordmark.

## Layout

The container is `min(1360px, calc(100% - 2 × gutter))`, centered. This supersedes the archived 1280px rule. Section padding is vertical, using the frontmatter section values. Gaps are authored per composition rather than enforced through an invented universal spacing scale.

| Width condition | Built response |
|---|---|
| Below 360px | Gutter 16px, compact header controls, 38px hero type, no headline sparkle, 310px wall, 22px brief-panel padding. |
| Default phone | Gutter 20px; stacked hero; two wall lanes in a 350px window; single-column work; 85%-width rail cards; 64px section padding. Below 600px the body reserves 75px for the floating action. |
| From 600px | Gutter 32px; three lanes / 440px wall; 12-column work grid with half-width cards and alternating 45px offsets; service and agency columns; three process columns; 45%-width rail cards. |
| From 1000px | Gutter 48px and section padding 90px; visible desktop navigation; split hero (1:1.15), 610px wall; asymmetrical 7/5 then 5/7 work spans; service visual/copy columns; split FAQ/contact; four-column footer; 37%-width rail cards capped at 590px. |
| From 1350px | 76px hero type; 640px wall; hero minimum height 690px; larger service gaps/type. |

Desktop work deliberately varies aspect ratio and offset. Filtering removes offsets and uses half-width cards with a consistent image ratio. On phone, the message and enquiry precede the contained wall. The rail uses native horizontal overflow, snap points, touch scrolling and explicit previous/next buttons; it never hijacks page scrolling. Anchor scrolling reserves 105px for the sticky header.

The header is 78px minimum on smaller layouts and 88px from 1000px. It starts forest and becomes cream after the hero leaves view. At widths below 1000px, JS provides a menu toggle while preserving the visible header enquiry action. The floating enquiry appears when the hero is out of view and contact is not visible, hides for an open dialog, and is disabled at desktop widths. This behavior requires IntersectionObserver/JS; it is not the only contact path.

## Elevation & Depth

Large sections use tonal blocks, image cropping and overlap rather than floating card shells. Photography supplies physical shadows; the 360° seal is the main visibly lifted decorative object. UI shadows are localized:

| Role | Built CSS shadow |
|---|---|
| Primary-action hover | `0 5px 16px #062d261a` |
| Expanded compact navigation | `0 15px 20px #062d2614` |
| 360° seal | `0 9px 25px #062d263d` |
| Floating contact | `0 7px 25px #062d2626` |
| Project dialog | `0 18px 75px #0005` |

The modal backdrop is opaque forest tint (`#062d26e6`). Caption gradients are local to photographs; they preserve readable text without covering the page in effects. There is no backdrop-filter or ambient full-page blur system.

## Shapes

Images, form panel and project dialog share the image radius; the original logo sits on a small softly squared chip. Actions and metadata use pills, while icon wells, rail arrows and process symbols use circles. Form fields keep square edges and a single lower rule (`#8da39b`) rather than outlined boxes. Dividers use the shared line token. Inline SVG icons use one coherent stroke style, with the four-point sparkle recurring as the signature. The 3D sparkle is a brand illustration, not a replacement logo.

The wall rotates as one clipped composition (−6° phone, −7° desktop) with a slight scale and a vertical transparency mask. Cropping uses `overflow: clip`; the wall's moving tiles are decorative, not focusable project controls. Never restore moving tap targets or a scrollable internal wall crop.

## Components

### Navigation and actions

Use semantic anchors for destinations and buttons for state changes. The cream logo chip, three plain-language links, visible enquiry action and compact menu are the current navigation system. Menu toggles expose expanded state, close after selection, and close on Escape with focus restored. The skip link becomes visible on keyboard focus.

The primary pill has a minimum height of 52px and a contrasting circular arrow well. Hover turns its surface cream, adds the small local shadow and rotates the arrow (250ms). The form uses the forest variant with pale-gold icon well and teal hover. Text links use an underline, minimum height 46px and a short diagonal arrow translation. Header action minimum is 44px (45px desktop). Do not infer a blanket 44px minimum from the archive: current motion control, some footer links and phone rail arrows are smaller. General focus outlines are 3px teal with 5px offset; dark header/hero/agency/contact contexts use pale gold, and form fields use 2px teal.

### Campaign wall and motion

The wall demonstrates breadth without moving the actual reading or action targets. Eight distinct images from seven retained brand worlds populate two duplicated vertical lanes. Tiles preserve each complete 3:2 composition; stage clipping belongs to the continuous wall rather than the individual photograph. The center seal was removed so it cannot cover products. The stage is `aria-hidden`; a visible fictional-concept label and accessible Pause/Lecture control sit outside it. Stable gallery and rail buttons expose the work separately.

CSS translates each track by −50% in a linear loop. The two lanes run at 43s and 54s reversed, with −3s/−50s offsets. Explicit pause persists per tab in sessionStorage and updates `aria-pressed`, icon and label. Hover on hover-capable devices and stage focus-within temporarily pause tracks. Page visibility and offscreen observation pause them too. Opening a project adds the sleeping state; closing resynchronizes visibility. Continuous animation is transform-only; no animation framework, video, WebGL or requestAnimationFrame scroll loop is involved.

Entry choreography is limited to the italic display phrase (800ms) and the wall stage (900ms), using `cubic-bezier(.16,1,.3,1)`. The earlier direction's proposed 700ms tile entrance is intent, not the built duration. Work-card appearance fades over 350ms; service-panel opacity changes over 230ms using WAAPI; ordinary feedback mostly uses 200–250ms transitions. No repeated section fly-ins are built.

Reduced motion disables loop and entry animations, card animation and smooth anchor scrolling; removes wall rotation; uses fixed lane offsets; hides the unnecessary motion control; suppresses image zoom/arrow spatial hover transforms; skips service crossfade; and makes rail-button scrolling immediate. Short color/background feedback remains. This is source-inspected behavior, not an OS-preference browser test.

### Work gallery, filters and project dialog

Seven brand articles show sixteen complete 3:2 campaign images, with a primary image, one or two secondary views, project titles, example briefs and deliverables. Concept labels sit below the primary image; controls do not overlap artwork. The “Explorer” hover treatment is supplementary; the whole card remains touch/keyboard operable. Filters are a labelled group of pill buttons using `aria-pressed`; hidden cards leave layout and the polite status announces counts. All seven remain visible by default without JS.

The native modal dialog supplies the fictional-concept toolbar, large image, title, scope, deliverable chips, disclosure and contact link. It has explicit close/previous/next controls, arrow-key cycling, Escape, outside-click close and return focus to the opener. The dialog sequence contains the seven homepage brand families, independent of the selected gallery filter. Thumbnail buttons select each family’s two or three images; Left/Right selects images, while the labelled previous/next controls change brands. The initial thumbnail button opens its own image, with focus restored on close. Body scrolling is locked while it is open. The horizontal rail revisits Pulse, Palma, Muse and Grain, linking to the same brand albums.

### Service selector

Four visible task tabs name the offer directly: Stratégie, Branding, Présence digitale, Événements. This section sits before the example gallery. Each panel pairs an uncropped landscape concept with a specific example, concrete deliverables and a contact link. Website/e-commerce and social media are explicit. The selected tab gets a short underline transition and the panel uses a bounded 320ms mask/opacity change. Reduced motion skips the panel animation.

Native buttons retain tablist/tab/tabpanel relationships, roving tabindex, arrow keys and Home/End. Hero expertise links activate the corresponding tab. All panel images remain 3:2 at every breakpoint; mobile uses a two-by-two tab grid, desktop four columns. Contact links preselect their exact form option using data-need, not positional indexes. Without JavaScript all service panels remain readable.

### Partners, agency and imagery

Partner logos come from incumbent assets, visibly labelled **“Les partenaires de Magic 360”**; they do not authenticate the fictional portfolio. Keep the six partner assets separate from concept cards. The agency section now pairs a tactile generated hands/paper scene with a smaller inset of the new Naya hands campaign. The process scene caption explicitly calls it an imagined/generated scene, never a photograph of Magic’s actual team or office.

Generated imagery provenance and exact prompts are preserved in [ASSETS.json](ASSETS.json) (Zéra, Horizon, Rencontres, Maison Nūr, Soli) and [MOTION-ASSETS.json](MOTION-ASSETS.json) (Naya, Kora, Saison, Muse, Magic object). Both record built-in image_gen sources. HUMAN-ASSETS.json adds Pulse, Grain, Palma and a clearly illustrated creative-table scene, with four new masters and responsive derivatives. Original 1536×1024 PNG masters remain asset sources; pages use 480/900/1400 WebP variants via srcset/sizes, not the PNG masters. Nine wall images are eager, lower-page images lazy, with reserved dimensions and async decoding. The actual logo is a non-recolored resized transparent PNG (352×160), preserving incumbent identity. Generation does not establish real commissions, real premises, results, testimonials or partner associations.

### Process, FAQ and enquiry

The three-step process uses ruled connections only at desktop widths and circular stroke symbols. FAQ uses native details/summary, a plus-to-close rotation and ruled rows. It remains usable without JS.

The brief panel has three labelled fields: required name (maxlength 100), need select, required message (maxlength 2000). Native constraint validation blocks an empty draft; custom French validity messages also reject whitespace-only names/messages. Editing a prepared field removes the stale draft URL and asks the visitor to prepare the updated draft. Submit prepares an encoded link to `https://wa.me/21696913500?text=…` containing the entered name, need and message. A polite status explains that a draft is ready and focus moves to **“Ouvrir mon brouillon WhatsApp.”** Nothing is sent automatically; the visitor follows the link and reviews in WhatsApp. Values stay in the fields; no backend submission or saved lead is implemented. Phone (`+21696913500`) and email (`contact@magic360.tn`) are direct alternatives; Tunis, Tunisie remains the published locality. Without JS the draft/gallery interaction is unavailable and the noscript note points to direct contact.

## Do's and Don'ts

### Do:
- **Do** use the living campaign wall, stable controls and varied imagery as one coherent current system.
- **Do** preserve the original logo and Magic's forest, cream and pale-gold frame.
- **Do** retain visible fictional labels in gallery, service imagery, rail and dialog, separately from partners.
- **Do** preserve pause, reduced motion, keyboard navigation, native details/dialog and direct contact alternatives.
- **Do** rebuild current root HTML with `build_magic.py` and keep this document aligned with the actual CSS/JS.
- **Do** treat local finish review as review evidence and conversion improvement as an unmeasured hypothesis.

### Don't:
- **Don't** apply the archived five prototypes' container, spacing or comparison controls to the current root by default.
- **Don't** turn photographic campaign colors into a replacement UI palette or recolor the original identity.
- **Don't** make moving wall tiles clickable, add scroll hijacking, a custom cursor or repeated section fly-ins.
- **Don't** present generated concepts as client projects, partners as concept clients, or the sparkle illustration as real premises.
- **Don't** describe the WhatsApp draft as a sent enquiry or promise a response time that is not evidenced.
- **Don't** claim production deployment, conversion gains, awards, measured Web Vitals or certified accessibility from local review.

## 2026-10-29 image expansion

User retained the accepted bold, artistic world and asked for clearer scope, more examples, more campaign imagery and better positioning. Nine new selected built-in Imagegen masters plus responsive 480/900/1400 WebP derivatives are recorded in CLARITY-ASSETS.json and BRAND-EXPANSION-ASSETS.json. Seven homepage families show sixteen images: Naya (3), Palma (3), Grain (2), Kora (2), Muse (2), Saison (2), Pulse (2). Existing reference assets informed the six campaign extensions. Fictional labels remain visible.

Zéra, Rencontres, Soli, Maison Nūr, Horizon and the gold ornament are absent from the current root and its project data. Their source assets and earlier archived directions are preserved. The active page references no assets/concepts images. The mobile floating contact bar is removed so it cannot obscure images; sticky header retains contact access. Main images, secondary views, service images, rail and dialog all use contain at the source landscape ratio. Only the decorative continuous wall clips its moving stage.

Verification: qa-clarity/ and QA-CLARITY.md. Bounded local browser pass checked 320, 390, 614, 1024 and 1440px, image ratios, filter counts, service keyboard selection, album navigation/focus and contact draft behavior. Detector ran once in degraded regex mode; no findings. No deployment or message sent.


## Hero creative replacement — 2026-11-01

User requested the same 14-image scale as Superside, stronger creative variety, and replacement of poorly proportioned existing hero images. Active hero now contains 14 original fictional-brand creatives: MIRO, POGO, FORMA, TEMPO, BLOOM, RIVE, ONDA, ALTO, TERA, ORBIT, LUMA, NORI, FOLIO and FABLE. Art spans beauty, food, architecture/editorial, music, hospitality, sport, fintech, jewelry and fashion. Reference supplies composition and proportions; artwork is original. Existing Magic identity and copy remain.

Built-in ImageGen masters and 480/900/1400 WebP derivatives live in assets/hero/. Exact prompts, source paths and actual dimensions: HERO-CREATIVE-ASSETS.json. Most assets use .68 or .907 width/height proportions, with one square variant. Each tile follows its artwork's intrinsic ratio; image fit is contain. Desktop retains three moving columns; mobile retains two 200px-high moving rows with variable tile widths. Only stage boundaries clip the moving wall.

Hero editor includes the complete new collection first, complete artwork previews and native-aspect uploads. Upload derivatives cap height at 4096px; srcset descriptors use actual generated widths. Previous hero selection is preserved in content/hero-before-portrait-20261101.json. Older files remain available without appearing in active hero rotation.

## Lime Studio selected — 2026-11-03

User selected palette 1. Forest #102F29, logo/action green #0B6959, ivory #F5F8EE, lime #D8F36A, sage surface #E2EAD7. Muted copy #436052 is derived for legibility. Main hero CTA uses logo green with white text; navigation and headline use lime. Existing WhatsApp green and campaign artwork retain their identity. Font options are proposals until user selection.

## Outfit + DM Sans selected — 2026-11-03

User selected option outfit. Outfit 800 for h1/h2/h3 and their colored emphasis; upright treatment supersedes earlier Fraunces italics. DM Sans 400–700 for body, navigation, buttons and fields. French accents supported by local Latin/Latin Extended WOFF2 fonts with font-display swap; source licenses retained. Existing type scale, content, motion and Lime Studio colors preserved. Font CSS and primary fonts use updated preload/cache references.

## Shared horizontal section spacing — 2026-11-03

User requested both section edges align with hero text. All section containers now use the hero width/gutters: 16px below768px, 32px at768–1279px, centered1216px at1280–1649px, centered1608px from1650px. Exploration rail uses the same bounded viewport with no extra horizontal padding; header centers on that container above1920px too. Hero campaign wall retains its existing full-bleed geometry. Component/form/dialog inner spacing remains independent.

## Rubans signature partner section — 2026-11-03

User selected Rubans signature from five previews. Centered Outfit 500 heading, original relationship label, two monochrome logo rows on Lime Studio ivory, opposing 48s/54s linear loops and soft lateral masks. All 12 partners verified from magicbrandingco.com are included once accessibly; repeated groups are aria-hidden with empty alt text. Row groups span at least the visible container to keep the loop seamless. Original partner assets retained; trimmed, scaled, lossless WebP derivatives serve the ribbons. Latest user refinement removes the partner pause/resume control and saved pause preference; offscreen/hidden sections still sleep. Reduced motion and no-JavaScript fallback show all original logos in static grids. Content viewport uses shared hero gutters; existing hero artwork and typography stay intact.

Partner optical adjustments, 2026-11-03: Pharmacie Centrale image width120px desktop/106px phone, enlarged from94/82px. SPAUZ uses intrinsic aspect ratio and CSS inset(3.5% 2%) to hide only the baked-in outer frame; source artwork stays intact. Per-partner data attributes apply adjustments consistently to both moving copies and static fallback.

## Magic proposition section — 2026-11-03

User selected Sortir du cadre, concept2, from generated images. New #notre-approche section sits directly between partners and expertise. It follows supplied reference: left uppercase label/rule, large two-part headline, supporting statement, body and dark contact CTA; right square campaign image with12px corners. Desktop from1280px uses equal columns with64px gap (80px from1650px); smaller viewports stack text before image. All content uses shared hero-aligned container and selected Outfit/DM Sans/Lime Studio. Image retains complete square composition and a small generated-illustration caption; original1254px PNG and480/900/1254px WebP derivatives retained. Text explains Magic’s strategy, branding, digital and experience services through the problem of disconnected brand touchpoints. Exact copy, prompts and image provenance: ABOUT-SECTION-OPTIONS.json.

## Selected editorial solutions — 2026-11-04

User selected the sage editorial solutions section for the original homepage, directly after services and before the agency. Three alternating copy/interface spreads cover tailored platforms, automation and applications. Existing forest/lime/ivory palette and Outfit/DM Sans remain. Illustrative HTML/CSS interfaces are static visual examples; real CTA links preselect matching contact needs. Header and footer now link to #solutions. Root contains exactly one solutions section and no proposal comparison overlays. Shared rendering in solution_variants.py keeps main and preview content consistent through future builder/admin saves.

## Selected editorial services — 2026-11-04

L’éditorial is selected. Four open editorial category groups preserve enamel icons, Outfit headings, DM Sans text and hero-aligned gutters. Each category header pairs its title/intent with explanatory copy and a need-specific contact link; below, three unboxed image/text features span equal columns. Mobile stacks them in order. Fine forest separators, ivory surface and generous spacing continue the proposition section. Images retain complete3:2 framing with12px corners; responsive480/800/1200px WebP, lazy loading, reserved ratio. Eleven new tactile campaign images and retained Muse event illustrate twelve individual services. Forest/lime strategy imagery, VELA branding, ONDA digital and MUSE events extend the hero art direction. Exact prompts/provenance: SERVICE-EDITORIAL-ASSETS.json. No service tabs or compare bar on the selected preview. Root and editorial route share the source.
