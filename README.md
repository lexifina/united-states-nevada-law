# United States (Nevada): law history in git

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is the law of Nevada, United States, which global-law reads at `united-states/nevada/acts/`.

A first build of Nevada law as git: one file per provision, with the text published by the Nevada Legislature (Legislative Counsel Bureau) ([leg.state.nv.us](https://www.leg.state.nv.us/NRS/)). It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `united-states/nevada/`. Language: English.

**What is in it now**

| Folder | Law | Versions | History |
| --- | --- | ---: | --- |
| `constitution/` | Constitution of the State of Nevada (1864, as amended) | 1 | Oldest version available (retrieved 2026-07-13 or 2026-10-23 (the Internet Archive capture day of each page)) |
| `nrs-193/` | NRS chapter 193: Criminality Generally | 1 | Oldest version available (retrieved 2026-07-13 or 2026-10-23 (the Internet Archive capture day of each page)) |
| `nrs-200/` | NRS chapter 200: Crimes Against the Person | 1 | Oldest version available (retrieved 2026-07-13 or 2026-10-23 (the Internet Archive capture day of each page)) |
| `nrs-205/` | NRS chapter 205: Crimes Against Property | 1 | Oldest version available (retrieved 2026-07-13 or 2026-10-23 (the Internet Archive capture day of each page)) |
| `nrs-111/` | NRS chapter 111: Estates in Property | 1 | Oldest version available (retrieved 2026-07-13 or 2026-10-23 (the Internet Archive capture day of each page)) |
| `nrs-001/` | NRS chapter 1: Judicial department generally | 1 | Oldest version available, dated 2026-09-09 (93 sections) |
| `nrs-001a/` | NRS chapter 1A: Judicial retirement | 1 | Oldest version available, dated 2026-04-15 (72 sections) |
| `nrs-002/` | NRS chapter 2: Supreme court | 1 | Oldest version available, dated 2024-06-29 (59 sections) |
| `nrs-002a/` | NRS chapter 2A: Court of appeals | 1 | Oldest version available, dated 2026-04-15 (26 sections) |
| `nrs-003/` | NRS chapter 3: District courts | 1 | Oldest version available, dated 2026-04-15 (80 sections) |
| `nrs-004/` | NRS chapter 4: Justice courts | 1 | Oldest version available, dated 2026-04-15 (68 sections) |
| `nrs-005/` | NRS chapter 5: Municipal courts | 1 | Oldest version available, dated 2026-09-09 (28 sections) |
| `nrs-006/` | NRS chapter 6: Juries | 1 | Oldest version available, dated 2024-06-29 (19 sections) |
| `nrs-007/` | NRS chapter 7: Attorneys and counselors at law | 1 | Oldest version available, dated 2026-04-15 (24 sections) |
| `nrs-010/` | NRS chapter 10: General provisions | 1 | Oldest version available, dated 2026-04-15 (20 sections) |
| `nrs-218f/` | NRS chapter 218F: Legislative counsel bureau | 1 | Oldest version available, dated 2026-04-15 (31 sections) |
| `nrs-220/` | NRS chapter 220: Revision of statutes | 1 | Oldest version available, dated 2024-06-29 (16 sections) |

A section the page prints twice (for example a text in force from a later day) keeps both texts, in page order.

## What it does not show

Each text therefore has one commit, "oldest version available", credited to the publisher and dated by the retrieval day.
- **Other law.** NRS chapters whose page no web archive holds (as itself, not a challenge page) are not yet included.
- **Notes.** Source notes, histories and annotations are not law text and are not in the files.

## How it is checked

Every version names its source and the sha256 of the data it was read from. Each version is read back from git and must match `corpus.json` (`tools/check_repo.py`); the results are in `REPRODUCE.md`.

## Sources

| Source | Kind | Past versions | Licence |
| --- | --- | --- | --- |
| [the Nevada Legislature (Legislative Counsel Bureau)](https://www.leg.state.nv.us/NRS/) | Official publisher | no | Statute text is not copyrightable (Georgia v. Public.Resource.Org, 2020) |

## Licence

See `LICENSE`. This repository is not legal advice and not an official publication.
