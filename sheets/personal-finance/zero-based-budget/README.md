# Zero-Based Budget

**Category:** Personal Finance

**Summary:** I'd use this when I want every dollar spoken for before the month starts, not just tracked after the fact. It pairs a transaction log with a 12 month plan and a variance sheet, so it's easy to see where the plan held up and where it slipped. Good fit for someone who wants tighter control than a simple spending tracker gives them.

**Structure:** `Setup` holds monthly income, grouped budget categories, default plan amounts, and the remainder check that should land on zero. `Transactions` is the raw log with date, payee, amount, category, and payment method dropdowns. `Monthly Plan` mirrors the category list across Jan to Dec, with each month defaulting back to `Setup` and an annual total at the end. `Actuals vs Plan` pulls actual spending with `SUMPRODUCT` by month and category, then calculates variance for every category and month. `Trends` rolls that into monthly income, total spent, surplus or deficit, a rolling 3 month spend average, and the two charts.
