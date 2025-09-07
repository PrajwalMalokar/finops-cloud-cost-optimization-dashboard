import sqlite3,os
from dotenv import load_dotenv
load_dotenv(override=True)

DB_PATH = os.getenv("DATABASE_NAME")

def update_status():
    conn = sqlite3.connect(DB_PATH)
    curr = conn.cursor()

    curr.execute("SELECT id, service, usage_quantity, usage_unit FROM usage")
    rows = curr.fetchall()

    for row in rows:
        row_id, service, usage_quantity, usage_unit = row
        status = "Safe"

        try:
            qty = float(usage_quantity)
        except:
            qty = 0  

        if service == "AmazonEC2" and qty > 720:
            status = "At-Risk"
        elif service == "AmazonS3" and qty > 5:
            status = "At-Risk"
        elif service == "AmazonRDS" and qty > 720:
            status = "At-Risk"
        elif service == "AmazonLambda" and qty > 1000000:
            status = "At-Risk"
        elif service == "AmazonCloudWatch" and qty > 1000:
            status = "At-Risk"

        curr.execute("UPDATE usage SET status=? WHERE id=?", (status, row_id))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    update_status()
    print("Status updated successfully!")
