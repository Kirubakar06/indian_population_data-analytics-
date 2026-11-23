"""
Perform analytical calculations and summaries.
"""
import pandas as pd


def create_analysis(dataframe: pd.DataFrame) -> dict[str, pd.DataFrame]:
    top_population = dataframe.nlargest(10, "Population_2011")[
        ["State_Name", "Population_2011", "Population_Rank"]
    ]
    top_literacy = dataframe.nlargest(10, "Literacy_Rate")[
        ["State_Name", "Literacy_Rate", "Population_Rank"]
    ]
    density_ranking = dataframe.nlargest(10, "Population_Density")[
        ["State_Name", "Population_Density", "Population_Rank"]
    ]

    summary = pd.DataFrame(
        {
            "Metric": [
                "Total Population",
                "Average Literacy Rate",
                "Largest State by Area",
                "Highest Population Density",
            ],
            "Value": [
                dataframe["Population_2011"].sum(),
                dataframe["Literacy_Rate"].mean(),
                dataframe.loc[
                    dataframe["State_Area_SqKm"].idxmax(), "State_Name"
                ],
                dataframe.loc[
                    dataframe["Population_Density"].idxmax(), "State_Name"
                ],
            ],
        }
    )

    return {
        "summary": summary,
        "top_population": top_population,
        "top_literacy": top_literacy,
        "density_ranking": density_ranking,
    }
