# Refi Or Paydown

**Category:** Personal Finance

**Summary:** I'd use this when a refinance quote looks tempting, but the real choice is wider than just rate shopping. It lines up the refinance, extra-paydown, and invest-the-difference paths so you can see payment changes, balance changes, and a rough net-worth view over the same hold period. Good for a homeowner who wants the decision in one place before paying fees or locking a rate.

**Structure:** `Inputs` keeps the current mortgage, refi quote, extra principal amount, investment return assumption, home appreciation, and the payment math from `PMT`. `Refi Case`, `Extra Paydown Case`, and `Invest Case` each run a year-by-year path for remaining balance, home value, equity, annual payment, and a net-worth proxy. `Extra Paydown Case` also shows the payoff check. `Break-Even & Summary` compares Year 1 and Year 10 outcomes, calculates the hold-period break-even with `MINIFS`, and keeps the net-worth, break-even, and interest-vs-market charts together.
