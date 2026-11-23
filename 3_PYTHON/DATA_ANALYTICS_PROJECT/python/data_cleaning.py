"""
Clean and prepare the source data.
"""
import pandas as pd


REQUIRED_COLUMNS = [
    "State_ID",
    "State_Name",
    "Population_2011",
    "Literacy_Rate",
    "State_Area_SqKm",
    "Population_Rank",
]


def clean_data(dataframe: pd.DataFrame) -> pd.DataFrame:
    missing_columns = [column for column in REQUIRED_COLUMNS if column not in dataframe.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")

    cleaned = dataframe.copy()
    cleaned["State_Name"] = cleaned["State_Name"].astype(str).str.strip()
    numeric_columns = [
        "State_ID",
        "Population_2011",
        "Literacy_Rate",
        "State_Area_SqKm",
        "Population_Rank",
    ]
    for column in numeric_columns:
        cleaned[column] = pd.to_numeric(cleaned[column], errors="coerce")

    cleaned = cleaned.dropna(subset=REQUIRED_COLUMNS)
    cleaned = cleaned.drop_duplicates(subset=["State_ID", "State_Name"])
    cleaned["Population_Density"] = (
        cleaned["Population_2011"] / cleaned["State_Area_SqKm"]
    )
    return cleaned.sort_values("Population_Rank").reset_index(drop=True)
