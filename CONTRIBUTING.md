# Contributing to ModelStack

Thanks for thinking about adding something. Seriously. This whole thing started because a few of us kept emailing spreadsheets back and forth and finally said "why don't we just put these somewhere?"

If you've got a sheet that's been sitting in your Google Drive for two years doing real work, it probably belongs here.

## The short version

1. Fork the repo
2. Add your spreadsheet in `sheets/your-sheet-name/`
3. Include a short `README.md` in that folder (what it does, how it's laid out)
4. Open a PR

That's it. We'll take a look and merge it if it fits.

## Folder structure

Each spreadsheet gets its own folder under `sheets/`:

```
sheets/
  your-sheet-name/
    your-sheet-name.xlsx
    README.md
```

If your project includes supporting files (a Python script that generates the sheet, a CSV data source, whatever), just toss them in the same folder. We're not strict about it.

The README doesn't need to be long. Just tell us what the sheet does, who it's for, and walk through the tabs and any formulas worth mentioning. Write it like you're explaining it to a coworker, not writing a product page.

## What we're looking for

Honestly? Anything useful. Budgeting tools, business trackers, financial models, planning sheets, analytics dashboards... if it helps someone get a job done, we're interested. Some examples of stuff we'd love to get:

- A rental property cash flow tracker someone's been using for their duplex
- A freelancer's quarterly tax estimator
- A meal planning budget sheet (yeah, that counts)
- An options wheel strategy log
- A simple savings goal tracker with a progress bar
- A full DCF model with sensitivity tables
- A project cost estimator with Gantt-style timelines

We don't really care if it's polished. Some of the best sheets in here started as something someone threw together on a Sunday afternoon. If it works, it works.

## A couple things to keep in mind

- Clear out your personal data before submitting. Replace your actual numbers with sample data... obviously.
- Sheets should open without errors in Excel. Bonus points if they work in Google Sheets or LibreOffice too, but Excel is the baseline.

## Writing style

Keep it casual. We're not writing whitepapers here. When you write your README:

- Use "I" and "we" freely. "I built this to track my side hustle income" is better than "This spreadsheet enables income tracking for supplementary revenue streams."
- Be specific. Name the tabs, mention the formulas, call out what's clever about it.
- Short is fine. A few sentences per section works. Don't pad it.

## Questions?

Open an issue. Or if you're not sure whether your sheet fits, just ask. We'd rather talk about it than have you spend time prepping a PR that doesn't land.
