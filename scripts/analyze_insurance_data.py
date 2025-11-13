import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect("healthcare_data.db")

# 1️⃣ Preview first few rows
print("\n🔹 Preview Data:")
df = pd.read_sql_query("SELECT * FROM insurance_claims LIMIT 5;", conn)
print(df)

# 2️⃣ Average claim amount by region
print("\n🔹 Average Claim Amount by Region:")
query_region = """
SELECT hospital_region AS region,
       ROUND(AVG(claim_amount), 2) AS avg_claim,
       COUNT(*) AS num_claims
FROM insurance_claims
GROUP BY hospital_region
ORDER BY avg_claim DESC;
"""
print(pd.read_sql_query(query_region, conn))

# 3️⃣ Average claim by smoker status
print("\n🔹 Average Claim Amount by Smoker Status:")
query_smoker = """
SELECT smoker_status,
       ROUND(AVG(claim_amount), 2) AS avg_claim
FROM insurance_claims
GROUP BY smoker_status;
"""
print(pd.read_sql_query(query_smoker, conn))

# 4️⃣ Correlation between age and claim amount
print("\n🔹 Correlation between Age and Claim Amount:")
query_age = """
SELECT age, claim_amount FROM insurance_claims;
"""
df_corr = pd.read_sql_query(query_age, conn)
print(df_corr.corr())

conn.close()
