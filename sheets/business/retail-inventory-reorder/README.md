# Retail Inventory Reorder

**Category:** Business

**Summary:** Inventory and reorder sheet for a small kitchen supply shop called The Copper Whisk. It tracks what's in stock, flags when something drops below the reorder point, and groups pending orders by supplier so you can hit order minimums. Good fit for any small retail operation where you're managing 30-50 SKUs by hand and don't want to miss a restock.

**Structure:** `Inventory` lists every product with SKU, name, category, current stock, reorder point, reorder qty, unit cost, markup, sell price, supplier, last ordered date, and notes. A default markup percent and low-stock alert threshold sit at the top. `Suppliers` is a directory with contact info, phone, email, order minimum, payment terms, lead time, account number, and notes for each vendor. `Reorder Queue` collects items that need ordering, grouped by supplier, with quantity needed, unit cost, line total, an ordered-yes/no flag, and notes.
