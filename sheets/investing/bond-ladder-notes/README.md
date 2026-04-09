# Bond Ladder Notes

**Category:** Investing

**Summary:** This is the kind of sheet I'd keep open while spacing out bond maturities for retirement income. It shows when coupon cash lands, when principal comes back, and what changes if you roll maturities into new bonds instead of spending the cash. Best fit for a retiree, planner, or anyone who wants the ladder math in one place without a full bond-desk model.

**Structure:** `Ladder Setup` is the bond list with type, purchase date, maturity date, coupon, price, frequency, and a `Reinvest At Maturity` flag, plus weighted-average checks on the right. `Cash Flow Schedule` uses `SUMPRODUCT` to roll coupon income and maturity principal into yearly cash flow from 2027 to 2036. `Reinvestment View` turns those maturities into new coupon income with a user-set reinvestment rate and term. `Summary & Sensitivity` pulls the ladder totals, adds the reinvestment grid, and keeps the three visuals together: maturity timing, annual cash by year, and yield by maturity.
