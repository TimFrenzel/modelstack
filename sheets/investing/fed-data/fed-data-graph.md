# fed-data-graph



**Category:** Investing

**Summary:** Excel file with 20 key macro indicators from January 2006 to December 2025 with easy line chart visualization. The file already includes the following macro indicators fetched from FRED and can be manipulated to include more data for different time periods.

This file can be used for easy reference to macro data, for data ingestion into other databases, extracted for data analysis (e.g., regression with portfolio returns), or for other time series analysis.

**Structure:** The `macro_panel_2006_2025_monthly` tab includes 20 macro indicators with dates in columns A to U. Columns W to Y display 2 user-selected macro indicators  through a pull-down menu in cells X1 and Y1. holds monthly returns for the target portfolio/mutual fund and benchmark. The `Formulas` tab computes VAMI, Underwater, Market Capture, Maximum Drawdown, Sortino Ratio, Rolling Volatility, Rolling Beta, Rolling Alpha, and VaR.

**Index, FRED Series, and Description**

All data is pulled from FRED via their public REST API (`api.stlouisfed.org`). The following series are included:

| Column                           | FRED Series     | Description                                        |
| -------------------------------- | --------------- | -------------------------------------------------- |
| `pce_price_index`                | PCEPI           | PCE Price Index                                    |
| `core_pce_price_index`           | PCEPILFE        | Core PCE Price Index (ex food & energy)            |
| `fed_funds_rate`                 | FEDFUNDS        | Effective Federal Funds Rate                       |
| `real_gdp_growth_annualized_qoq` | A191RL1Q225SBEA | Real GDP Growth (annualized, quarter-over-quarter) |
| `ust_10y_yield`                  | DGS10           | 10-Year Treasury Yield                             |
| `ust_2y_yield`                   | DGS2            | 2-Year Treasury Yield                              |
| `yield_curve_10y_2y`             | T10Y2Y          | 10Y-2Y Treasury Spread                             |
| `unemployment_rate`              | UNRATE          | Civilian Unemployment Rate                         |
| `nonfarm_payrolls`               | PAYEMS          | Total Nonfarm Payrolls                             |
| `consumer_sentiment`             | UMCSENT         | University of Michigan Consumer Sentiment          |
| `wti_oil_price`                  | DCOILWTICO      | WTI Crude Oil Price                                |
| `initial_jobless_claims`         | ICSA            | Initial Jobless Claims                             |
| `housing_starts`                 | HOUST           | Housing Starts                                     |
| `baa_corp_spread_10y`            | BAA10YM         | Baa Corporate Bond Spread over 10Y Treasury        |
| `nfci`                           | NFCI            | Chicago Fed National Financial Conditions Index    |

See https://github.com/michaelshpan/fed-data for Python script to fetch FRED data and more details on the data source.