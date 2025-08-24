import boto3,os
from dotenv import load_dotenv
load_dotenv(override=True)

AWS_REGION = os.getenv("AWS_REGION")
client=boto3.client("ce",region_name=AWS_REGION)

response = client.get_cost_and_usage(
    TimePeriod={"Start": "2025-03-01", "End": "2025-03-31"},
    Granularity="MONTHLY",
    Metrics=["UnblendedCost", "UsageQuantity"],
    GroupBy=[
        {"Type": "DIMENSION", "Key": "SERVICE"},
        {"Type": "DIMENSION", "Key": "USAGE_TYPE"}
    ]
)
## Sample Response
# {
#   "ResultsByTime": [
#     {
#       "TimePeriod": {"Start": "2025-08-01", "End": "2025-08-02"},
#       "Total": {},
#       "Groups": [
#         {
#           "Keys": ["AmazonEC2", "BoxUsage:t2.micro"],
#           "Metrics": {
#             "UsageQuantity": {"Amount": "24.0", "Unit": "Hrs"},
#             "UnblendedCost": {"Amount": "0.00", "Unit": "USD"}
#           }
#         },
#         {
#           "Keys": ["AmazonS3", "TimedStorage-ByteHrs"],
#           "Metrics": {
#             "UsageQuantity": {"Amount": "1024.0", "Unit": "GB-Mo"},
#             "UnblendedCost": {"Amount": "0.00", "Unit": "USD"}
#           }
#         }
#       ]
#     }
#   ]
# }

rows = []
for result in response["ResultsByTime"]:
    date=result["TimePeriod"]["Start"]
    for group in result["Groups"]:
        service = group["Keys"][0]
        usage_type = group["Keys"][1]
        usage_quantity = float(group["Metrics"]["UsageQuantity"]["Amount"])
        unblended_cost = float(group["Metrics"]["UnblendedCost"]["Amount"])
        rows.append({
            "Date": date,
            "Service": service,
            "UsageType": usage_type,
            "UsageQuantity": f"{usage_quantity} {group['Metrics']['UsageQuantity']['Unit']}",
            "CostINR": unblended_cost * 82.0 # 1 USD = 82 INR
        })
