import sqlite3, os
from dotenv import load_dotenv
import pandas as pd
from fetch_api import rows

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
            usage_quantity TEXT,
            cost_inr REAL
            )''')



df = pd.DataFrame(rows)

for _,row in df.iterrows():
    curr.execute('''
                INSERT INTO usage (date,service, usage_type, usage_quantity, cost_inr)
                VALUES(?,?,?,?,?)
                ''',(row["Date"],row["Service"],row["UsageType"],row["UsageQuantity"],row["CostINR"]))
    
curr.execute("SELECT * FROM usage LIMIT 5")
print(curr.fetchall())

conn.commit()
curr.close()
conn.close()