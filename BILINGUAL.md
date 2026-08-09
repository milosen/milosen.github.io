# Bilingual setup (English / German)

The site is served in two languages: English at the root (`/`) and German
under `/de/`. A compact `EN|DE` control in the navbar switches between them.

The switcher only links to the other language when a counterpart actually
exists. Where it does not, the control renders greyed out with a tooltip
instead of linking to a missing page — so partial translation is a normal,
supported state, not a broken one.

## Adding a blog post

### A post in one language only

Write it as usual and set `lang` in the front matter:

```yaml
---
layout: null
title: "Some post"
date: 2026-08-09
lang: en          # or: de
---
```

It appears on the homepage for that language only. The language button on
the post shows the other language greyed out.

`lang: en` is the default, so an English post works even without the field —
but setting it explicitly is clearer.

### A post in both languages

Write two files and give them the **same `translation_key`**:

```yaml
# _posts/2026-08-09-my-post.html
---
layout: null
title: "The shape of things"
date: 2026-08-09
lang: en
translation_key: shape-of-things
---
```

```yaml
# _posts/2026-08-09-my-post-de.html
---
layout: null
title: "Die Gestalt der Dinge"
date: 2026-08-09
lang: de
translation_key: shape-of-things
---
```

The key is an arbitrary identifier — any string, as long as both files agree.
The switcher pairs them automatically in both directions, and each post gets a
small `DE` / `EN` badge in the homepage list marking that a translation exists.

### The language bar on standalone posts

Posts using `layout: null` are complete HTML documents and do not inherit the
site navbar. Add the bar yourself, directly after `<body>`:

```liquid
<body>
{% include post_chrome.html %}
```

It carries both the "back to homepage" link (pointing at the homepage in the
post's own language) and the language switcher, and ships its own styles, so it
works inside a self-contained essay without pulling in the site stylesheet. It
supports light and dark colour schemes.

Also make the document's language attribute follow the front matter:

```liquid
<html lang="{{ page.lang | default: site.default_lang }}">
```

Posts that use a normal Jekyll layout get the navbar and switcher for free.

## Adding or changing interface text

All interface strings live in `_data/i18n.yml`, keyed by language. Add a key
under **both** `en` and `de`, then use it in a template:

```liquid
{%- assign lang = page.lang | default: site.default_lang -%}
{%- assign t = site.data.i18n[lang] -%}
{{ t.blog_posts }}
```

Never hardcode a user-visible English string in a template — put it in
`i18n.yml` and reference it, otherwise it will leak onto the German pages.

## Profile, education, awards, news

These are language-keyed maps in `_data/profile.yml` and `_news/*.md`:

```yaml
short_bio:
  en: >-
    ...
  de: >-
    ...
```

News items fall back to the default language when a translation is missing, so
an untranslated item still shows up rather than rendering blank.

## Adding a static page

1. Create the English page with `lang: en` and a `permalink`.
2. Create the German mirror at `de/<name>.html` with `lang: de` and
   `permalink: /de/<name>`.
3. Add `translated: true` to **both**. This enables the switcher's mirrored
   path convention (`/foo` <-> `/de/foo`) and emits `hreflang` tags for search
   engines.
4. Add the page to both language lists in `_data/navigation.yml`, using a
   shared `key`, and add `nav_<key>` labels to `_data/i18n.yml`.
5. Set `navbar_key: <key>` in both pages' front matter so the active nav item
   highlights.

Omit `translated: true` when a page genuinely has no counterpart — that is what
`/more` currently does, since its cards are free-form English content. The
switcher then correctly reports the page as unavailable in the other language.

If two pages are translations but do not follow the mirrored path convention,
set `translation_url` explicitly in the front matter; it overrides everything
else.

## Not yet translated

- The two existing essays are English-only. Adding German versions is the
  `translation_key` flow above; nothing else needs to change.
- The `/more` page cards (`_more/default/*.md`) are still English.
