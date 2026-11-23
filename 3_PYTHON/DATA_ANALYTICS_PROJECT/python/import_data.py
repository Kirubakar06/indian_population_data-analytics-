"""
Load source data for analysis.
"""
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_DATA_PATH = PROJECT_ROOT / "01_EXCEL" / "India_States_Analytics.csv.xlsx"


def import_excel(file_path: Path = DEFAULT_DATA_PATH) -> pd.DataFrame:
    if not file_path.exists():
        raise FileNotFoundError(f"Dataset not found: {file_path}")
    return pd.read_excel(file_path)
