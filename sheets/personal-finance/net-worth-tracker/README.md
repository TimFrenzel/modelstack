# Net Worth Tracker

**Category:** Personal Finance

**Summary:** I'd use this as a steady monthly check-in file. It keeps assets, liabilities, history, and milestone dates together so the trend is easy to read instead of scattered across apps and account sites. Good fit for someone who updates balances once a month and wants a clean picture of how the gap is moving.

**Structure:** `Accounts` stores the account list, institution, type, asset or liability lookup, opening balance, and opening date. `Monthly Balances` gives each account a Jan to Dec row and then totals assets, liabilities, net worth, and month over month change below the table. `History` keeps a longer 24 month view with 3 month, 6 month, and 12 month rolling average change. `Milestones` compares the latest net worth against target amounts and projects months and dates using the trailing 6 month growth pace. `Dashboard` brings together the net worth trend, assets versus liabilities area chart, current balance by asset type, and milestone progress table.
