import pandas as pd
import os

os.makedirs("database", exist_ok=True)
os.makedirs("models", exist_ok=True)
os.makedirs("datasets", exist_ok=True)

# Basic initial database
pd.DataFrame(columns=["FarmerID", "FarmerName", "Village", "Acres", "RiceType"]).to_csv("database/farmers.csv", index=False)
pd.DataFrame(columns=["BookingID", "FarmerName", "SlotTime", "VehicleNo", "Status"]).to_csv("database/bookings.csv", index=False)

print("🚀 Clean project directories and empty databases initialized!")