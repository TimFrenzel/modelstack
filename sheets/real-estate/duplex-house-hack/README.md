# Duplex House Hack

**Category:** Real Estate

**Summary:** This one is for the buyer who's asking a personal question, not a landlord question: after the other units pay rent, what does it really cost me to live here? It keeps the loan, rent roll, monthly housing cost, and a few decision checks in one workbook. Good fit for a duplex or triplex buyer who wants to compare the deal against just staying in their current rental.

**Structure:** `Property & Loan` holds the purchase price, FHA-style down payment, loan payment from `PMT`, taxes, insurance, PMI, reserves, current-rent alternative, and the quick-read box. `Unit Rent Roll` stores one owner unit plus the rentable units and calculates net rent to owner after utility share. `Monthly Housing Cost` turns that into a 12-month owner-cost view with vacancy loss, effective tenant rent, owner net housing cost, and savings versus current rent. `Scenario Grid` adds the occupancy and rent matrix, a cost bridge, a simple swing table, and the three visuals. `Snapshot` keeps the owner-cost answer and worst-case housing cost on one short page.
