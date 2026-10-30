# United States (Nevada): law history in git

A first build of Nevada law as git: one file per provision, with the text published by the Nevada Legislature (Legislative Counsel Bureau) ([leg.state.nv.us](https://www.leg.state.nv.us/NRS/)). It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `united-states/nevada/`. Language: English.

**What is in it now**

| Folder | Law | Versions | History |
| --- | --- | ---: | --- |
| `constitution/` | Constitution of the State of Nevada (1864, as amended) | 1 | Oldest version available (retrieved 2026-07-13 or 2026-10-23 (the Internet Archive capture day of each page)) |
| `nrs-193/` | NRS chapter 193: Criminality Generally | 1 | Oldest version available (retrieved 2026-07-13 or 2026-10-23 (the Internet Archive capture day of each page)) |
| `nrs-200/` | NRS chapter 200: Crimes Against the Person | 1 | Oldest version available (retrieved 2026-07-13 or 2026-10-23 (the Internet Archive capture day of each page)) |
| `nrs-205/` | NRS chapter 205: Crimes Against Property | 1 | Oldest version available (retrieved 2026-07-13 or 2026-10-23 (the Internet Archive capture day of each page)) |
| `nrs-111/` | NRS chapter 111: Estates in Property | 1 | Oldest version available (retrieved 2026-07-13 or 2026-10-23 (the Internet Archive capture day of each page)) |

## What it does not show

Each text therefore has one commit, "oldest version available", credited to the publisher and dated by the retrieval day.
- **Other law.** The rest of the Nevada Revised Statutes is not yet included; NRS chapter 78 (private corporations) has no Internet Archive capture.
- **Notes.** Source notes, histories and annotations are not law text and are not in the files.

## How it is checked

Every version names its source and the sha256 of the data it was read from. Each version is read back from git and must match `corpus.json` (`tools/check_repo.py`); the results are in `REPRODUCE.md`.

## Sources

| Source | Kind | Past versions | Licence |
| --- | --- | --- | --- |
| [the Nevada Legislature (Legislative Counsel Bureau)](https://www.leg.state.nv.us/NRS/) | Official publisher | no | Statute text is not copyrightable (Georgia v. Public.Resource.Org, 2020) |

## Licence

See `LICENSE`. This repository is not legal advice and not an official publication.
