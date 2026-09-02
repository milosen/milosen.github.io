# milosen.github.io

Personal academic homepage. Plain static HTML — no Jekyll, no build step,
no JavaScript. GitHub Pages serves the files exactly as they are in this
repository (`.nojekyll` disables Jekyll processing).

## Layout

```
index.html              English homepage
publications.html       English publication list
de/index.html           German homepage
de/publications.html    German publication list
404.html
feed.xml                News feed
assets/style.css        The entire stylesheet
assets/cv.pdf           CV (built from assets/cv/main.tex)
```

## Editing

Edit the HTML directly — that is the whole workflow. Open a file, change the
text, commit. To preview locally:

```sh
python3 -m http.server 8000     # then open http://localhost:8000
```

### Adding a publication

Copy an existing `<article class="pub">` block in `publications.html` and edit
it. Add it to `index.html` too if it should appear under "Selected
publications". Keep the same block in both language versions — titles,
venues and abstracts stay in English in both.

### Adding a news item

Copy a `<div class="news-item">` block in `index.html` and `de/index.html`,
newest first, and add a matching `<item>` to `feed.xml`.

### Language switching

Each page links to its counterpart through the `EN / DE` control in the
header. If you add a page in one language only, point its language link at
the other language's homepage, or render it as `<span class="off">` so it
is visibly unavailable rather than broken.

## Regenerating

`_src/build.py` generated these pages once from the old Jekyll content
(`_src/content.json`). It is kept for reference only; the HTML files are now
the source of truth and are edited by hand. The previous Jekyll site is
preserved under `_archive/`.
