# -*- coding: utf-8 -*-
"""One-off generator: turns the extracted Jekyll content into plain HTML.
After this runs the site is static; this script is not needed to serve it."""
import json, html, io, os, re

C = json.load(open('/tmp/content.json', encoding='utf-8'))
ME = "Nikola Milosevic"
OUT = '/tmp/newsite/out'

T = {
 'en': dict(lang='en', other='de', otherlabel='DE',
    nav_home='Home', nav_pubs='Publications', nav_cv='CV',
    role='Ph.D. Candidate, <a href="https://www.cbs.mpg.de/en">MPI CBS</a>, Leipzig',
    h_news='News', h_pubs='Selected publications', h_all='Publications',
    h_edu='Education', h_awards='Awards',
    abstract='Abstract', allpubs='All publications',
    updated='Last updated', backhome='Home',
    title_home='Nikola Milosevic', title_pubs='Publications — Nikola Milosevic',
    desc='Nikola Milosevic — Ph.D. researcher at MPI CBS working on reinforcement learning that is safe, well understood, and ready for the real world.',
    bio=['I’m a Ph.D. researcher at MPI CBS working on <a href="https://en.wikipedia.org/wiki/Reinforcement_learning">reinforcement learning</a> that is safe, well understood, and ready for the real world.',
         'Most RL breakthroughs live in simulators. Getting them to work under real-world constraints — safety requirements, limited data, deployment risk — is not just an engineering challenge, but the place where the hard and interesting theoretical problems are. I work on building a strong theoretical foundation for reinforcement learning for precisely these issues.'],
    edu=[('Max Planck Institute for Human Cognitive and Brain Sciences','Neural Data Science Lab · Ph.D. Candidate','2022 — present'),
         ('University of Applied Sciences Leipzig','M.Sc. Electrical Engineering','2019 — 2021')],
    awards=[('Master’s Thesis Award, University of Applied Sciences Leipzig','2021')]),
 'de': dict(lang='de', other='en', otherlabel='EN',
    nav_home='Start', nav_pubs='Publikationen', nav_cv='Lebenslauf',
    role='Doktorand, <a href="https://www.cbs.mpg.de/de">MPI CBS</a>, Leipzig',
    h_news='Aktuelles', h_pubs='Ausgewählte Publikationen', h_all='Publikationen',
    h_edu='Ausbildung', h_awards='Auszeichnungen',
    abstract='Zusammenfassung', allpubs='Alle Publikationen',
    updated='Zuletzt aktualisiert', backhome='Start',
    title_home='Nikola Milosevic', title_pubs='Publikationen — Nikola Milosevic',
    desc='Nikola Milosevic — Doktorand am MPI CBS, Forschung zu Reinforcement Learning, das sicher, theoretisch fundiert und praxistauglich ist.',
    bio=['Ich bin Doktorand am MPI CBS und forsche an <a href="https://de.wikipedia.org/wiki/Best%C3%A4rkendes_Lernen">Reinforcement Learning</a>, das sicher, theoretisch gut verstanden und praxistauglich ist.',
         'Die meisten Fortschritte im Reinforcement Learning entstehen in Simulationen. Sie unter realen Bedingungen zum Laufen zu bringen — mit Sicherheitsanforderungen, begrenzten Daten und Einsatzrisiken — ist nicht bloß eine ingenieurtechnische Aufgabe, sondern genau dort liegen die schwierigen und interessanten theoretischen Fragen. Ich arbeite daran, für ebendiese Fragen ein tragfähiges theoretisches Fundament zu schaffen.'],
    edu=[('Max-Planck-Institut für Kognitions- und Neurowissenschaften','Neural Data Science Lab · Doktorand','2022 — heute'),
         ('Hochschule für Technik, Wirtschaft und Kultur Leipzig','M.Sc. Elektrotechnik','2019 — 2021')],
    awards=[('Masterarbeitspreis der HTWK Leipzig','2021')]),
}

MONTH_DE = {1:'Jan.',2:'Feb.',3:'März',4:'Apr.',5:'Mai',6:'Juni',7:'Juli',8:'Aug.',9:'Sep.',10:'Okt.',11:'Nov.',12:'Dez.'}
MONTH_EN = {1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}

def e(s): return html.escape(s or '', quote=True)

def datestr(d, lang):
    y, m = int(d[:4]), int(d[5:7])
    return f"{(MONTH_DE if lang=='de' else MONTH_EN)[m]} {y}"

def authors_html(a):
    out = []
    for n in a:
        out.append(f'<span class="me">{e(n)}</span>' if n == ME else e(n))
    return ', '.join(out)

def head(t, desc, lang, css, canon, alt_en, alt_de):
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(t)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="en" href="{alt_en}">
<link rel="alternate" hreflang="de" href="{alt_de}">
<link rel="alternate" hreflang="x-default" href="{alt_en}">
<meta property="og:type" content="website">
<meta property="og:title" content="{e(t)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="https://milosen.github.io/assets/images/portrait.jpg">
<meta name="twitter:card" content="summary">
<meta name="twitter:site" content="@NikMilosevic">
<link rel="icon" type="image/svg+xml" href="{css.rsplit('/',1)[0]}/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Spectral:ital,wght@0,400;0,500;0,600;1,400&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{css}">
</head>
<body>'''

def masthead(t, page, prefix, counterpart):
    home = prefix + ('index.html' if prefix else '')
    home = prefix if prefix else './'
    pubs = (prefix or '') + 'publications.html'
    cur = lambda p: ' aria-current="page"' if p == page else ''
    lang_html = (f'<a href="{counterpart}" hreflang="{t["other"]}">{t["otherlabel"]}</a>'
                 if counterpart else f'<span class="off">{t["otherlabel"]}</span>')
    return f'''<header class="masthead wrap">
<a class="name" href="{home}">{ME}</a>
<nav>
<a href="{home}"{cur('home')}>{t['nav_home']}</a>
<a href="{pubs}"{cur('pubs')}>{t['nav_pubs']}</a>
<a href="{CVPATH}">{t['nav_cv']}</a>
<span class="lang"><span>{t['lang'].upper()}</span><span class="sep">/</span>{lang_html}</span>
</nav>
</header>'''

def footer(t, prefix):
    yr = '2026'
    return f'''<footer class="wrap">
<span>© {yr} {ME}</span>
<span class="right"><a href="{prefix}feed.xml">RSS</a></span>
</footer>
</body>
</html>'''

def pub_block(p, lang, t, idx):
    venue = ''
    if p['pub_pre']: venue += e(p['pub_pre'])
    if p['pub']:     venue += f"<em>{e(p['pub'])}</em>"
    if p['pub_post']: venue += e(p['pub_post'])
    links = []
    for k, v in p['links'].items():
        links.append(f'<a href="{e(v)}" rel="noopener">{e(k)}</a>')
    linkrow = '<span class="dot">·</span>'.join(links)
    abst = ''
    if p['abstract']:
        abst = (f'<details><summary>{t["abstract"]}</summary>'
                f'<p class="abstract">{e(p["abstract"])}</p></details>')
    return f'''<article class="pub">
<h3>{e(p['title'])}</h3>
<p class="authors">{authors_html(p['authors'])}</p>
<p class="venue">{venue}</p>
<p class="links">{linkrow}</p>
{abst}
</article>'''

CVPATH = ''

def build(lang):
    global CVPATH
    t = T[lang]
    prefix = '' if lang == 'en' else ''
    # asset + counterpart paths differ between root and /de/
    if lang == 'en':
        css, assets, counter_home, counter_pubs = 'assets/style.css', 'assets/', 'de/', 'de/publications.html'
        base, pfx = OUT, ''
    else:
        css, assets, counter_home, counter_pubs = '../assets/style.css', '../assets/', '../', '../publications.html'
        base, pfx = OUT + '/de', ''
    CVPATH = assets + 'cv.pdf'
    os.makedirs(base, exist_ok=True)

    U = 'https://milosen.github.io/'
    # ---------- home ----------
    news = '\n'.join(
        f'<div class="news-item"><time datetime="{n["date"][:10]}">{datestr(n["date"],lang)}</time>'
        f'<p>{n["title"][lang]}</p></div>' for n in C['news'])
    edu = '\n'.join(
        f'<div class="row-item"><span class="what">{e(a)}</span><span class="when">{e(c)}</span>'
        f'<span class="where">{e(b)}</span></div>' for a, b, c in t['edu'])
    awards = '\n'.join(
        f'<div class="row-item"><span class="what">{e(a)}</span><span class="when">{e(b)}</span></div>'
        for a, b in t['awards'])
    sel = [p for p in C['pubs'] if p['selected']]
    selhtml = '\n'.join(pub_block(p, lang, t, i) for i, p in enumerate(sel))
    bio = '\n'.join(f'<p>{x}</p>' for x in t['bio'])

    home = head(t['title_home'], t['desc'], lang, css,
                U + ('de/' if lang == 'de' else ''), U, U + 'de/')
    home += masthead(t, 'home', pfx, counter_home)
    home += f'''
<main>
<div class="wrap">
<div class="hero">
<h1>{ME}</h1>
<p class="role">{t['role']}</p>
<div class="bio">
{bio}
</div>
<div class="contact">
<a href="mailto:milose.nik&#64;gmail.com">milose.nik@gmail.com</a>
<a href="{assets}cv.pdf">CV (PDF)</a>
<a href="https://scholar.google.com/citations?user=vGYpn-sAAAAJ&amp;hl" rel="noopener">Google&nbsp;Scholar</a>
<a href="https://github.com/milosen" rel="noopener">GitHub</a>
<a href="https://orcid.org/0000-0003-1904-8867" rel="noopener">ORCID</a>
<a href="https://www.linkedin.com/in/nikola-milosevic-5061271a7" rel="noopener">LinkedIn</a>
</div>
</div>

<section>
<h2 class="sec-head">{t['h_news']}</h2>
<div class="news">
{news}
</div>
</section>

<section>
<h2 class="sec-head">{t['h_pubs']}</h2>
{selhtml}
<p class="more-link"><a href="{pfx}publications.html">{t['allpubs']} <span aria-hidden="true">→</span></a></p>
</section>

<section>
<h2 class="sec-head">{t['h_edu']}</h2>
<div class="rows">
{edu}
</div>
</section>

<section>
<h2 class="sec-head">{t['h_awards']}</h2>
<div class="rows">
{awards}
</div>
</section>
</div>
</main>
'''
    home += footer(t, assets.replace('assets/', ''))
    io.open(os.path.join(base, 'index.html'), 'w', encoding='utf-8').write(home)

    # ---------- publications ----------
    byyear = {}
    for p in C['pubs']:
        byyear.setdefault(p['pub_date'] or p['date'][:4], []).append(p)
    body = ''
    for y in sorted(byyear, reverse=True):
        body += f'<h2 class="year">{e(y)}</h2>\n'
        body += '\n'.join(pub_block(p, lang, t, i) for i, p in enumerate(byyear[y]))
    pubs = head(t['title_pubs'], t['desc'], lang, css,
                U + ('de/publications.html' if lang == 'de' else 'publications.html'),
                U + 'publications.html', U + 'de/publications.html')
    pubs += masthead(t, 'pubs', pfx, counter_pubs)
    pubs += f'''
<main>
<div class="wrap">
<div class="hero">
<h1>{t['h_all']}</h1>
</div>
<section style="margin-top:2.5rem">
{body}
</section>
</div>
</main>
'''
    pubs += footer(t, assets.replace('assets/', ''))
    io.open(os.path.join(base, 'publications.html'), 'w', encoding='utf-8').write(pubs)

for l in ('en', 'de'):
    build(l)
print('gebaut:', OUT)
