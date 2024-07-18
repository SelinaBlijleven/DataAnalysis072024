"""
relational_plots.py

The first important types of plots are the relational plots. This includes the
line plot and the scatter plot, which both illustrate the relationship between variables.
"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def generate_data(size: int = 100) -> pd.DataFrame:
    # Generate random data
    np.random.seed(42)
    data = pd.DataFrame({
        'x': np.arange(1, size + 1),
        'y': np.random.normal(loc=0, scale=1, size=size).cumsum(),
        'category': np.random.choice(['A', 'B', 'C'], size=100)
    })
    return data


def main():
    # Generate some dummy data
    data = generate_data()

    # Scatterplot
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='x', y='y', hue='category', data=data)
    plt.title('Scatterplot: Relationship between X and Y')
    plt.savefig("plots/scatterplot.png")

    # Lineplot
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='x', y='y', hue='category', data=data)
    plt.title('Lineplot: Relationship between X and Y')
    plt.savefig("plots/lineplot.png")


if __name__ == "__main__":
    main()
