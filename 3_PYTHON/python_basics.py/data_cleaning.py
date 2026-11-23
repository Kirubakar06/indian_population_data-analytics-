
import pandas as pd
from database_connection import engine

# Import MySQL data
df = pd.read_sql_query(
    "SELECT * FROM indian_states",
    engine
)

print("Original Data:")
print(df.head())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Remove duplicate records
df = df.drop_duplicates()

# Remove unwanted spaces from State_Name
df["State_Name"] = df["State_Name"].str.strip()

# Final cleaned data
print("\nCleaned Data:")
print(df.head())

# Export cleaned data
df.to_csv(
    "output/indian_states_cleaned.csv",
    index=False
)

df.to_excel(
    "output/indian_states_cleaned.xlsx",
    index=False
)

print("\nData Cleaning Completed!")
print("Cleaned files saved in output folder.")
