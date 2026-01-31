import pandas as pd
import sqlite3

# Load CSV
orders = pd.read_csv("orders.csv")

# Load JSON
users = pd.read_json("users.json")

# Load SQL into SQLite
conn = sqlite3.connect(":memory:")

with open("restaurants.sql", "r") as f:
    sql_script = f.read()

conn.executescript(sql_script)

restaurants = pd.read_sql("SELECT * FROM restaurants", conn)

# Merge datasets (LEFT JOIN)
final_df = orders.merge(users, how="left", on="user_id") \
                 .merge(restaurants, how="left", on="restaurant_id")

# Save final dataset
final_df.to_csv("final_food_delivery_dataset.csv", index=False)

print("final_food_delivery_dataset.csv created successfully!")
