# Local image editor

Run `python website/serve_local.py` from the project folder. Open http://127.0.0.1:8000/admin/ or use **Gérer les images** in the website footer.

The editor manages all three hero columns. Choose an existing image or upload JPG/PNG/WebP (10 MB, 24 megapixels maximum), edit its visible name, and reorder with drag and drop or arrow buttons. Move images between columns, add or remove entries (1–12 per column), then click **Enregistrer**. Reload the public page to see the saved result. **Annuler les modifications** restores the last saved selection. Removing an entry retains its source image.

Saved selection: website/content/hero.json. Uploaded images: assets/uploads/, resized to three WebP widths while preserving the original aspect ratio. The builder reads the saved selection and atomically rebuilds index.html; manual rebuilds preserve selections. Desktop shows three portrait columns; mobile distributes the saved images in two horizontal rows. Public tiles follow each image’s intrinsic ratio, with no crop. The new hero collection contains 14 original fictional brand creatives in assets/hero/. Repeated tracks cover the complete hero even with one selected image.

Password verifier: %LOCALAPPDATA%/Magic360/admin-auth.json, outside the web root. PBKDF2-SHA256 uses a random salt; no plaintext password appears in page sources. Server checks authenticated sessions, CSRF tokens, origins, uploads and asset selections. Sessions last eight hours and expire on restart. Server listens only on 127.0.0.1:8000; editor requires this Python server and does not run on static-only hosting.

Validation on 2026-10-29: password login, unauthenticated write denial, CSRF/origin denial, private-source denial, invalid upload rejection, upload normalization, escaped labels, stale-save conflict, save/restore and logout. Browser checks: reorder/save/reload persistence, add/remove, library search, replace, cross-column movement and discard. Desktop/mobile inspected; detector ran once in degraded mode, with typography advisories addressed. Evidence: qa-clarity/editor-desktop.png and editor-mobile.png. Existing selection restored after checks.
