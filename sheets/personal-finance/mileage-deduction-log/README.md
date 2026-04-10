# Mileage Deduction Log

**Category:** Personal Finance

**Summary:** This is for someone who drives for work (freelance, side gig, whatever) and wants to track mileage plus other deductible expenses in one file. It uses the 2026 IRS standard mileage rate and keeps a running tally of business miles, then adds a separate expense sheet for things like home office, phone, supplies, and subscriptions. The summary tab estimates tax savings so you can see whether the record-keeping is actually worth anything.

**Structure:** `01-mileage` has the IRS rate and odometer start at the top, then a running log with date, destination or purpose, start miles, end miles, trip miles, and business-use percent. YTD business miles and mileage deduction totals update automatically. `02-expenses` tracks non-mileage deductions with date, expense description, category, amount, deductible percent, deductible amount, receipt flag, and notes. Home office and phone business-use percentages sit at the top. `03-deduction-summary` pulls the mileage and expense totals together, applies federal, state, and self-employment tax rates, and estimates total tax savings by category.
