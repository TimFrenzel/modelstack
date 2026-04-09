# One Stock Risk Check

**Category:** Investing

**Summary:** I'd pull this up when one stock has quietly grown into too much of the whole balance sheet. It shows how big the position is, what a drawdown does to net worth, and what changes if the owner sells in pieces or puts on a simple hedge. Best fit for employer stock, an inherited holding, or one winner that got way out of line with everything else.

**Structure:** `Position & Inputs` holds the share count, current price, other assets and the target max concentration, then calculates current position value and weight. `Risk Scenarios` runs up and down price moves and compares hold, sell 25% now and sell 50% now side by side. `Sale Plan` links the target weight, current shares, sell pace, and current price into a 12-step ladder with proceeds, remaining shares, estimated net worth and concentration after each step. `Hedge Comparison` uses simple `MAX` and `MIN` payoff math to compare hold, partial sales, a protective put & collar. `Snapshot` pulls the current exposure, downside cases and the best-scoring response together.
