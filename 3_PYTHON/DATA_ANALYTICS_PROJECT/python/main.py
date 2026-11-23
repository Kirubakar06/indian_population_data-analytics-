"""
Run the complete Indian states population analytics pipeline.
"""
from pathlib import Path

from data_analysis import create_analysis
from data_cleaning import clean_data
from data_visualization import create_visualizations
from database_connection import (
    get_connection,
    get_sqlalchemy_engine,
    save_dataframe,
)
from import_data import import_excel


PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = PROJECT_ROOT / "output"


def main() -> None:
    source_data = import_excel()
    cleaned_data = clean_data(source_data)
    analysis_results = create_analysis(cleaned_data)

    output_tables = {
        "india_states": cleaned_data,
        "analysis_summary": analysis_results["summary"],
        "top_population": analysis_results["top_population"],
        "top_literacy": analysis_results["top_literacy"],
        "density_ranking": analysis_results["density_ranking"],
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for table_name, dataframe in output_tables.items():
        dataframe.to_csv(OUTPUT_DIR / f"{table_name}.csv", index=False)

    connection = get_connection()
    connection.close()

    engine = get_sqlalchemy_engine()
    try:
        for table_name, dataframe in output_tables.items():
            save_dataframe(engine, table_name, dataframe)
    finally:
        engine.dispose()

    chart_paths = create_visualizations(cleaned_data, OUTPUT_DIR)
    print(f"Processed {len(cleaned_data)} state records.")
    print("Saved 5 analytics tables to MySQL and CSV files to output.")
    print(f"Charts: {', '.join(path.name for path in chart_paths)}")


if __name__ == "__main__":
    main()
