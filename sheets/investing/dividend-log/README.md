# Dividend Log

**Category:** Investing

**Summary:** I'd reach for this when a dividend portfolio has grown past the point where a broker screen tells the full story. It tracks the cash paid, the shares added through DRIP, and what those extra shares do to annual income over time. Nice fit for someone with a handful of income names who wants a clean register they can keep up by hand.

**Structure:** `Holdings & Settings` stores ticker, starting shares, cost, current price, annual dividend, and a `DRIP?` switch, then calculates current value, cost basis, annual income, and yield on cost. `Dividend Log` is one row per pay date, with formulas for cash dividend, DRIP shares added, cash taken, and ending shares. `Reinvestment History` rolls those events up by month with `SUMPRODUCT`, cumulative shares added, and total shares outstanding. `Income & Yield Summary` pulls the current share count by ticker, compares DRIP against cash-taking income, and keeps the share-growth and income charts in one place.
