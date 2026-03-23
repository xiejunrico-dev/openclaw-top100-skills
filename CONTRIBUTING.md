# Contributing to OpenClaw Top 100

Thank you for helping keep this list the best it can be.

## How the List Works

The Top 100 is a **curated, dynamic** list — not a static archive. Every month, we review the list and may swap out skills that have become outdated, broken, or superseded by better alternatives.

## How to Nominate a Skill

Open an [Issue](../../issues/new) with the following information:

- **Skill name** (must exist in [openclaw-master-skills](https://github.com/LeoYeAI/openclaw-master-skills))
- **Category** it belongs to
- **Why it should replace** the current skill in that category (or why a new category is needed)
- **Evidence of quality**: active maintenance, clear description, community usage

## How to Submit a PR

1. Fork this repository
2. Add the new skill folder under `skills/`
3. Remove the skill you are replacing (same category, same or fewer total count)
4. Update `README.md` and `README.zh-CN.md` accordingly
5. Add an entry to `CHANGELOG.md`
6. Open a PR with a clear description of the swap

## Selection Criteria

| Criterion | Details |
|---|---|
| **Clarity** | The `SKILL.md` has a clear, non-empty description |
| **Universality** | Works across platforms (not macOS-only, not Windows-only) |
| **No broken deps** | All required CLIs or APIs are accessible |
| **No API key required** (preferred) | Free-tier or no-cost options are preferred |
| **Active maintenance** | Updated within the last 6 months |

## Code of Conduct

Be respectful. Nominations are evaluated on merit, not personal preference.
