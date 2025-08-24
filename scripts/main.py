import sqlite3, os
from dotenv import load_dotenv
import pandas as pd
from scripts.fetch_api import fetch_cost_data


load_dotenv(override=True)
DATABASE_NAME = os.getenv("DATABASE_NAME")

if not DATABASE_NAME:
    raise ValueError("Database name is not set")

conn = sqlite3.connect(DATABASE_NAME)
curr = conn.cursor()

curr.execute('''
            CREATE TABLE IF NOT EXISTS usage (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            service TEXT,
            usage_type TEXT,
            usage_quantity REAL,
            usage_unit TEXT,
            cost_inr REAL,
            UNIQUE(date, service, usage_type)
            )''')
rows=fetch_cost_data("2025-03-01","2025-03-31")
df = pd.DataFrame(rows)

for _,row in df.iterrows():
    curr.execute('''
                INSERT or IGNORE INTO usage (date,service, usage_type, usage_quantity,usage_unit, cost_inr)
                VALUES(?,?,?,?,?,?)
                ''',(row["Date"],row["Service"],row["UsageType"],row["UsageQuantity"],row["UsageUnit"],row["CostINR"]))

curr.execute("SELECT * FROM usage LIMIT 5")
print(curr.fetchall())

conn.commit()
curr.close()
conn.close()