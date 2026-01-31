# food-delivery-data-integration
This project integrates food delivery data from multiple formats: - Orders data (CSV) - User data (JSON) - Restaurant data (SQL)


## Description
This project integrates food delivery data from multiple formats:
- Orders data (CSV)
- User data (JSON)
- Restaurant data (SQL)

All datasets are merged using LEFT JOINs to create a single analysis-ready dataset.

## Files
- orders.csv – Order transactions
- users.json – User information
- restaurants.sql – Restaurant details (cuisine, rating)
- merge_data.py – Python script to merge datasets
- final_food_delivery_dataset.csv – Final integrated dataset

## Tools Used
- Python
- Pandas
- SQLite
- VS Code

## Output
A single consolidated CSV file used for analysis and reporting.
