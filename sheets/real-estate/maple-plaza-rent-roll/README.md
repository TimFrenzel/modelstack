# Maple Plaza Rent Roll

**Category:** Real Estate

**Summary:** I use this kind of sheet when a small strip center looks fine on the flyer, but the lease rollover feels shaky once you slow down and look at it. It tracks 6 suites, pushes each one through downtime, TI spend and leasing commissions, then rolls the result into a 5-year hold and exit view. Good fit for a local buyer, broker, or owner who wants to see how one vacancy or one rough renewal can change the deal.

**Structure:** `Center Overview` holds purchase price, loan terms, rent growth, downtime, TI allowance and the center-level expense inputs. `Rent Roll` is one row per suite with `Status` and `Roll Year` dropdowns, plus a `Current Annual Base Rent` formula. `Lease Rollover` runs base rent, CAM recovery, and TI / LC costs by suite across Years 1 to 5, with the rent logic switching from in-place rent to market rent in the roll year. `5-Year Pro Forma` pulls those totals into potential gross income, credit loss, NOI, debt service, cash flow after debt, and DSCR. `Exit & Snapshot` keeps the sale math in one place, including exit value, loan payoff, equity multiple and `IRR`.
