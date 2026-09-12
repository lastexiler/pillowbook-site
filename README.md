# 枕书 · PillowBook · まくらと本 — site

Static pages for the iOS reader 枕书 / PillowBook: feature introduction, privacy
policy and support, in 简体中文 / 繁體中文 / English / 日本語.

```
index.html            picks the visitor's language and redirects
zh-Hans/  zh-Hant/  en/  ja/
  index.html          features
  privacy.html        privacy policy
  support.html        help / FAQ
content/<lang>/     privacy.md, support.md — the legal drafts (Markdown, one per language)
assets/style.css, assets/icon.png
tools/build.py        feature-page text + generator; renders the Markdown too
```

Edit the feature text in `tools/build.py`, or the privacy / support Markdown in
`content/`, then:

```bash
python3 tools/build.py
```

The privacy policy and support pages were drafted against the app's actual
behaviour on 2026-09-13 (local-only data, user-sent feedback mail, StoreKit
purchases, Wi-Fi transfer over local HTTP, system authentication, file sharing
and backups). Their source of truth is `reports/legal/` in the app repository;
copy changes here and rebuild. Update them whenever the app gains a permission,
a purchase, a network feature or a new place it keeps data.

Hosted with GitHub Pages from the repository root.
