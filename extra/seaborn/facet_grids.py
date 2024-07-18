"""
facet_grids.py

Facet grids are useful for visualizing multiple subplots based on one or more categorical variables.
"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def generate_data(size: int = 100) -> pd.DataFrame:
    # Generate random data
    np.random.seed(42)
    data = pd.DataFrame({
        'x': np.random.rand(size) * 10,
        'y': np.random.rand(size) * 10 + np.random.normal(0, 2, size),
        'category': np.random.choice(['A', 'B'], size=size),
        'subcategory': np.random.choice(['X', 'Y'], size=size)
    })
    return data


def main():
    # Generate some dummy data
    data = generate_data()

    # FacetGrid
    g = sns.FacetGrid(data, col="category", row="subcategory")
    g.map(plt.scatter, "x", "y")
    g.add_legend()
    plt.savefig("plots/facetgrid.png")

    # Catplot
    sns.catplot(x="category", y="y", hue="subcategory", data=data, kind="box")
    plt.title('Catplot: Boxplot by Category and Subcategory')
    plt.savefig("plots/catplot.png")

    # LM plot with FacetGrid
    sns.lmplot(x='x', y='y', hue='category', col='subcategory', data=data)
    plt.title('LM Plot with FacetGrid: Relationship between X and Y by Subcategory')
    plt.savefig("plots/lmplot_facet.png")


if __name__ == "__main__":
    main()
