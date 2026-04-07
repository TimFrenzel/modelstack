# Mutual Fund Analytics v1



**Category:** Investing

**Summary:** A simple mutual fund return-based analytics Excel tool based on [Chris Cheng's ftk.xlsx](https://github.com/chris-kc-cheng/ftk-excel). 

Chris's file implements around 70 commonly used functions for time series analysis. All functions are written in plain Excel formulas as lambda functions, and stored in named ranges. No auxiliary cells or columns are used, and no VBA is involved. 

The Mutual Fund Analytics file uses the LAMBDA functions and structure of the file, adding visualization with VAMI, Underwater, 12M Rolling Vol & Beta, and 12M Rolling Alpha charts. It also added user-input functionality for target portfolio/mutual fund and benchmark monthly return time series.  

**Structure:** The `Data` tab holds monthly returns for the target portfolio/mutual fund and benchmark. The `Formulas` tab computes VAMI, Underwater, Market Capture, Maximum Drawdown, Sortino Ratio, Rolling Volatility, Rolling Beta, Rolling Alpha, and VaR.