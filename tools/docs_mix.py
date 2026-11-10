"""Brings repo/README.md and repo/jurisdiction.json up to date with the signed-off corpus.d/nrs-*.json parts (NRS
chapters from web-archive captures of the Legislature's chapter pages). Starts from the published README. No network.
    python -X utf8 docs_mix.py
"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
R = os.path.join(HERE, 'repo')
NL = '\n'
CD = os.path.join(HERE, 'corpus.d')


def key(x):
    return [int(y) if y.isdigit() else y for y in re.split(r'(\d+)', x)]


parts = [f for f in os.listdir(CD) if f.endswith('.json') and os.path.exists(os.path.join(CD, f[:-5] + '.PUBLISH'))]
acts = sorted((json.load(open(os.path.join(CD, f), encoding='utf-8'))['acts'][0] for f in parts), key=lambda a: key(a['slug']))
nsec = sum(len(a['versions'][0]['units']) for a in acts)
rows = ''.join(f"{NL}| `{a['slug']}/` | {a['title'].replace('Nevada Revised Statutes, chapter', 'NRS chapter')} | 1 | Oldest version available, dated {a['versions'][0]['from']} ({len(a['versions'][0]['units'])} sections) |" for a in acts)

t = open(os.path.join(R, 'README.md'), encoding='utf-8').read()
t = re.sub(r'\n\| `nrs-(?!193/|200/|205/|111/)[^\n]*', '', t)
i = t.index('| `nrs-111/` |')
j = t.index(NL, i)
t = t[:j] + rows + t[j:]
note = (f'Chapters added on 2026-11-10 ({len(acts)} chapters, {nsec} sections) are each read from the newest web-archive copy of '
        'the chapter page and dated by the revision stamp the page prints ("Rev. <date>"), or by the day of the copy when it has '
        'none; a section the page prints twice (for example a text in force from a later day) keeps both texts, in page order.')
t = re.sub(r'\nChapters added on 2026-11-10[^\n]*\n', '\n', t)
t = re.sub(r'\nA section the page prints twice[^\n]*\n', '\n', t)
k = t.index('## What it does not show')
t = t[:k] + note + NL + NL + t[k:]
t = t.replace('- **Other law.** The rest of the Nevada Revised Statutes is not yet included; NRS chapter 78 (private corporations) has no Internet Archive capture.',
              '- **Other law.** NRS chapters whose page no web archive holds (as itself, not a challenge page) are not yet included.')
open(os.path.join(R, 'README.md'), 'w', encoding='utf-8', newline=NL).write(t)
jp = os.path.join(R, 'jurisdiction.json')
j = json.load(open(jp, encoding='utf-8'))
j['build'] = f'built: Constitution and {len(acts) + 4} NRS chapters, one version each from web-archive captures'
open(jp, 'w', encoding='utf-8', newline=NL).write(json.dumps(j, ensure_ascii=False, indent=2) + NL)
print(len(acts), 'added chapters,', nsec, 'sections')
