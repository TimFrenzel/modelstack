# Contributing to ModelStack

Thanks for thinking about adding something. Seriously. This whole thing started because a few of us kept emailing spreadsheets back and forth and finally said "why don't we just put these somewhere?"

If you've got a sheet that's been sitting in your Google Drive for two years doing real work, it probably belongs here.

## The short version

1. Fork the repo
2. Add your spreadsheet in `sheets/your-sheet-name/`
3. Include a short `README.md` in that folder (what it does, how it's laid out)
4. Open a PR

That's it. We'll take a look and merge it if it fits.

## File rules

- `.xlsx` only. No `.xls`, no `.xlsm`, no Google Sheets links.
- No macros. If it needs VBA to work, it's out of scope for this repo.
- Formulas, conditional formatting, data validation, pivot tables... all good. The fancier the better, honestly.
- Should open without errors in Excel. Bonus points if it works in Google Sheets and LibreOffice too, but Excel is the baseline.

## Folder structure

Each spreadsheet gets its own folder under `sheets/`:

```
sheets/
  your-sheet-name/
    your-sheet-name.xlsx
    README.md
```

The README doesn't need to be long. Just tell us what the sheet does, who it's for, and walk through the tabs and any formulas worth mentioning. Write it like you're explaining it to a coworker, not writing a product page.

## What we're looking for

Anything that helps someone manage money, track a business, plan for retirement, or just figure out where their paycheck went. Some examples of stuff we'd love to get:

- A rental property cash flow tracker someone's been using for their duplex
- A freelancer's quarterly tax estimator
- A meal planning budget sheet (yeah, that counts)
- An options wheel strategy log
- A simple savings goal tracker with a progress bar

We don't really care if it's polished. Some of the best sheets in here started as something someone threw together on a Sunday afternoon. If it works, it works.

## What we're NOT looking for

- Investment banking models (DCF, M&A, comps, etc.). Tons of repos do that already.
- Sheets behind paywalls or that require a login to download
- Anything with personal data still in it. Clear out your actual numbers before submitting... obviously.
- Sheets that are basically empty templates with no formulas or logic. We want tools, not blank grids.

## Writing style

Keep it casual. We're not writing whitepapers here. When you write your README:

- Use "I" and "we" freely. "I built this to track my side hustle income" is better than "This spreadsheet enables income tracking for supplementary revenue streams."
- Be specific. Name the tabs, mention the formulas, call out what's clever about it.
- Short is fine. A few sentences per section works. Don't pad it.

## Questions?

Open an issue. Or if you're not sure whether your sheet fits, just ask. We'd rather talk about it than have you spend time prepping a PR that doesn't land.
