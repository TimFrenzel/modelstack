# Estimated Quarterly Tax

**Category:** Personal Finance

**Summary:** I'd use this if I had both W-2 and 1099 income and needed to figure out quarterly estimated payments without paying someone to do it. It pulls prior-year AGI for safe harbor, logs every income payment as it comes in, and calculates what each quarter's check should be. The reference tab keeps the rate brackets and SE tax math in one place so you're not Googling it every quarter.

**Structure:** `01-quarterly-calc` starts with filing status, prior-year AGI, prior-year total tax, and the safe harbor amount, then runs each quarter's W-2 income, 1099 income, estimated SE tax, withholding, cumulative liability, and payment due. `02-income-log` is a raw transaction log with date, client or source, description, amount, income type (W-2 or 1099), quarter, and notes. `03-tax-reference` collects the key rates in one place: federal brackets, standard deduction, SE tax rate, state rate, and safe harbor rules, so everything the calc sheet references is visible on one tab.
