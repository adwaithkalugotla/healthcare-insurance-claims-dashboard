import sqlite3
import pandas as pd

# Load the dataset
df = pd.read_csv("../data/insurance.csv")

# Connect to SQLite database
conn = sqlite3.connect("../healthcare_data.db")

# Rename columns to fit our 'claims' theme
df = df.rename(columns={
    "age": "age",
    "sex": "gender",
    "bmi": "bmi",
    "children": "dependents",
    "smoker": "smoker_status",
    "region": "hospital_region",
    "charges": "claim_amount"
})

# Save data to a new table
df.to_sql("insurance_claims", conn, if_exists="replace", index=False)
conn.close()

print("✅ Insurance data successfully loaded into SQLite database!")
