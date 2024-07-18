"""
categorical_plots.py

Categorical plots help understand the distribution of categorical data and the relationship between categorical and numerical data.
"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def generate_data(size: int = 100) -> pd.DataFrame:
    # Generate random data
    np.random.seed(42)
    data = pd.DataFrame({
        'x': np.random.choice(['A', 'B', 'C'], size=size),
        'y': np.random.normal(loc=0, scale=1, size=size),
        'category': np.random.choice(['D', 'E', 'F'], size=size)
    })
    return data


def main():
    # Generate some dummy data
    data = generate_data()

    # Barplot
    plt.figure(figsize=(10, 6))
    sns.barplot(x='x', y='y', hue='category', data=data)
    plt.title('Barplot: Central Tendency of Y by X and Category')
    plt.savefig("barplot.png")

    # Countplot
    plt.figure(figsize=(10, 6))
    sns.countplot(x='x', hue='category', data=data)
    plt.title('Countplot: Counts of X by Category')
    plt.savefig("countplot.png")

    # Boxplot
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='x', y='y', hue='category', data=data)
    plt.title('Boxplot: Distribution of Y by X and Category')
    plt.savefig("boxplot.png")

    # Violinplot
    plt.figure(figsize=(10, 6))
    sns.violinplot(x='x', y='y', hue='category', data=data, split=True)
    plt.title('Violinplot: Distribution of Y by X and Category')
    plt.savefig("violinplot.png")


if __name__ == "__main__":
    main()
