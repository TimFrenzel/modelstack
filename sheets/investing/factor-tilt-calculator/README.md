# Factor Tilt Calculator

**Category:** Investing

**Summary:** I use this sheet to check how a single stock or portfolio leans across common equity factors, then I sanity-check the stats before making any allocation change. You paste monthly returns in one place, and the workbook calculates alpha, factor betas, p-values, and a few risk-adjusted metrics. It's best for someone who already tracks returns monthly and wants a quick read on market, size, value, and momentum exposure.

**Structure:** The `Data` tab holds monthly inputs in yellow cells for Date, Stock Return, Risk-Free Rate, Mkt-RF, SMB, HML, and MOM. The `Calculations` tab computes excess returns, runs `LINEST` for coefficients and standard errors, then derives t-stats and p-values with `T.DIST.2T`. It also shows annualized excess return, Sharpe ratio, active return, tracking error, and information ratio. The `Summary` tab pulls the key outputs into one compact table, and `Source Info` lists the data sources plus setup notes.
