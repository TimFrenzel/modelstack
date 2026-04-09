# SaaS MRR Notes

**Category:** Business

**Summary:** I'd use this when a small SaaS business is growing, but the monthly story still feels fuzzy. It keeps churn, expansion, paid acquisition, and month-12 margin in one file, so you can see if new bookings are actually replacing what leaks out. Good fit for a founder, operator, or part-time finance owner who wants a working sheet instead of a bigger finance stack.

**Structure:** `Business Inputs` holds starting customers, ARPA, churn, expansion, contraction, gross margin, fixed OpEx, and the pull from paid acquisition. `Monthly MRR Bridge` runs the 12-month customer and revenue walk, with `ROUND(Start * churn,0)` for churned logos, `End MRR / end customers` for ARPA, and the operating-margin line subtracting both fixed OpEx and paid spend. `Cohort Retention` keeps the first six cohorts on one grid, then `Acquisition & Unit Economics` rolls spend into blended `CAC`, lifetime, gross `LTV`, payback, and a quick ratio. `Snapshot & Scenarios` is the short read, with ending MRR, ARR, quick ratio, and a base / upside / downside table plus the charts.
