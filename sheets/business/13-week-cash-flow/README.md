# 13-Week Cash Flow

**Category:** Business

**Summary:** Built this for a small landscaping company that needed to know one thing: will cash run out before summer? Weeks 1 through 7 have actuals filled in, weeks 8 through 13 are forecasts. It's a working document, not a template. The sub-detail rows name actual jobs, clients, and notes about rain delays and upcoming payments. Anyone running a seasonal service business with lumpy income and fixed weekly payroll could drop their own numbers in here pretty quickly.

**Structure:** `Cash Flow` is a single sheet. The top section shows starting cash, projected ending cash at week 13, lowest cash point (a simple `MIN`), and weeks of runway if no new income lands. The main grid runs 13 weeks across columns for expected inflows, actual inflows, variance, payroll, rent, insurance, fuel and equipment, materials, other expenses, total outflows, net cash flow, and ending cash. Each week gets a sub-detail row naming the jobs and clients behind that week's numbers. Ending cash cascades from week to week. An `IF` formula switches between actual and expected inflows depending on what's filled in. Free-form notes at the bottom cover upcoming expenses and client situations.
