# Magic production delivery

Production origin: https://magicbrandingco.com/. The original VPS site is managed as the root PM2 application `magic_agency`, behind the existing nginx TLS vhost.

Versioned source includes the compiled homepage, selected editorial sections, builder, saved hero choices, optimized WebP/PNG icons, fonts and generation prompts. Large generated PNG masters remain locally in `assets/` and in the local `codex/full-source-local-backup` Git snapshot. Runtime and the hero editor use the optimized WebP collection; they do not require those masters. Do not delete them from the authoring workspace.

Run `python website/build_magic.py` to rebuild. For deployment, use `python website/build_public.py --output <new-empty-directory>/public --manifest <new-empty-directory>/manifest.json`. This copies the public site and delivery images, preserving complete aspect ratios. Source, credentials, QA artifacts, PDFs, local editor backend and bitmap masters stay outside the served directory.

The public server uses `website/serve.production.json`: no directory listings or SPA fallback. Serve the generated `public` directory on loopback port3000; keep the existing nginx TLS proxy. The image-editor footer link is available only on localhost. No public editor backend is deployed.

Before an update, read `/root/CLAUDE.md`, back up the existing repository and PM2 definition, stage a complete release, verify manifest hashes, and test it before switching. Preserve the old release and an explicit rollback command. Test external HTTPS from outside the VPS; its own public-IP curl bypasses UFW and does not prove external access. Avoid changes to unrelated services, nginx vhosts, firewall rules or credentials.
