
import pandas as pd
from database_connection import engine

# Import data from MySQL
query = """
SELECT *
FROM indian_states;
"""

df = pd.read_sql_query(query, engine)

# Display imported data
print("Data Imported Successfully!")

print("\nFirst 5 Records:")
print(df.head())

print("\nTotal Rows and Columns:")
print(df.shape)

print("\nColumn Information:")
print(df.info())
