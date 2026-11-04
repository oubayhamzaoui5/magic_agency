# Magic production delivery

Live frontend release: `4a73bf55877f7057193e9dccba074ba1a86f18f8`, deployed2026-11-04. Later documentation-only commits do not change its public bytes.

Current server source: `/root/magic_agency`; PM2 config: `/root/magic-runtime/ecosystem.config.json`. Previous release and configuration backups: `/root/magic-deploy-backups/20261104-39343f7/`. Roll back with `bash /root/magic-runtime/rollback-be38a82.sh`; it exchanges the release directories atomically and restores the original Magic PM2 configuration. Keep these backups and scripts root-only.

Production origin: https://magicbrandingco.com/. The original VPS site is managed as the root PM2 application `magic_agency`, behind the existing nginx TLS vhost.

Versioned source includes the compiled homepage, selected editorial sections, builder, saved hero choices, optimized WebP/PNG icons, fonts and generation prompts. Large generated PNG masters remain locally in `assets/` and in the local `codex/full-source-local-backup` Git snapshot. Runtime and the hero editor use the optimized WebP collection; they do not require those masters. Do not delete them from the authoring workspace.

Run `python website/build_magic.py` to rebuild. For deployment, use `python website/build_public.py --output <new-empty-directory>/public --manifest <new-empty-directory>/manifest.json`. This copies the public site and delivery images, preserving complete aspect ratios. Source, credentials, QA artifacts, PDFs, local editor backend and bitmap masters stay outside the served directory.

The public server uses `website/serve.production.json`: no directory listings or SPA fallback, with an exact root rewrite to `index.html`. Serve the generated `public` directory on loopback port3000; keep the existing nginx TLS proxy. The image-editor footer link is available only on localhost. No public editor backend is deployed.

On this Linux VPS, generate `public` using `--live-links` from a clean Git checkout and enable `serve -S`. Only the approved static entry points link to versioned files; source and repository metadata have no public route. This keeps the existing dashboard’s Git pull/restart workflow working without copying a stale compiled tree. The main repository remains `/root/magic_agency`; PM2 serves its `/public` directory. Build to a fresh directory and verify the manifest and private-path responses before switching.

Before an update, read `/root/CLAUDE.md`, back up the existing repository and PM2 definition, stage a complete release, verify manifest hashes, and test it before switching. Preserve the old release and an explicit rollback command. Test external HTTPS from outside the VPS; its own public-IP curl bypasses UFW and does not prove external access. Avoid changes to unrelated services, nginx vhosts, firewall rules or credentials.
