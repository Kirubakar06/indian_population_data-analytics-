
import pandas as pd
from database_connection import engine

# Import data
df = pd.read_sql_query(
    "SELECT * FROM indian_states",
    engine
)

# Total Population
total_population = df["Population_2011"].sum()

print("Total Population:")
print(total_population)

# Average Literacy Rate
average_literacy = df["Literacy_Rate"].mean()

print("\nAverage Literacy Rate:")
print(round(average_literacy, 2))

# Highest Population State
highest_population = df.loc[
    df["Population_2011"].idxmax()
]

print("\nHighest Population State:")
print(highest_population["State_Name"])

# Lowest Population State
lowest_population = df.loc[
    df["Population_2011"].idxmin()
]

print("\nLowest Population State:")
print(lowest_population["State_Name"])

# State-wise Population Ranking
population_ranking = df.sort_values(
    by="Population_2011",
    ascending=False
)

print("\nTop 5 Population States:")
print(
    population_ranking[
        ["State_Name", "Population_2011"]
    ].head(5)
)

print("\nData Analysis Completed!")
