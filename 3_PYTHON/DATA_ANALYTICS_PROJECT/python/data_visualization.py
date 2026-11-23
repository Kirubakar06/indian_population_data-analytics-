"""
Create charts and reports.
"""
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


def create_visualizations(
    dataframe: pd.DataFrame,
    output_dir: Path,
) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    generated_files: list[Path] = []

    top_population = dataframe.nlargest(10, "Population_2011")
    figure, axis = plt.subplots(figsize=(11, 7))
    axis.barh(top_population["State_Name"], top_population["Population_2011"])
    axis.invert_yaxis()
    axis.set_title("Top 10 States by Population (2011)")
    axis.set_xlabel("Population")
    figure.tight_layout()
    population_path = output_dir / "top_10_population.png"
    figure.savefig(population_path, dpi=150)
    plt.close(figure)
    generated_files.append(population_path)

    top_literacy = dataframe.nlargest(10, "Literacy_Rate")
    figure, axis = plt.subplots(figsize=(11, 7))
    axis.barh(top_literacy["State_Name"], top_literacy["Literacy_Rate"])
    axis.invert_yaxis()
    axis.set_title("Top 10 States by Literacy Rate")
    axis.set_xlabel("Literacy Rate (%)")
    axis.set_xlim(0, 100)
    figure.tight_layout()
    literacy_path = output_dir / "top_10_literacy.png"
    figure.savefig(literacy_path, dpi=150)
    plt.close(figure)
    generated_files.append(literacy_path)

    figure, axis = plt.subplots(figsize=(9, 7))
    axis.scatter(
        dataframe["Literacy_Rate"],
        dataframe["Population_Density"],
        alpha=0.75,
    )
    axis.set_title("Literacy Rate vs Population Density")
    axis.set_xlabel("Literacy Rate (%)")
    axis.set_ylabel("Population Density")
    figure.tight_layout()
    scatter_path = output_dir / "literacy_vs_density.png"
    figure.savefig(scatter_path, dpi=150)
    plt.close(figure)
    generated_files.append(scatter_path)

    return generated_files
