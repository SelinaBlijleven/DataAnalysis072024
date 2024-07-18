"""
distribution_plots.py

Distribution plots are useful for understanding the distribution of a single variable and comparing distributions
between subsets of data.
"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def generate_data(size: int = 100) -> pd.DataFrame:
    # Generate random data
    np.random.seed(42)
    data = pd.DataFrame({
        'x': np.random.normal(loc=0, scale=1, size=size),
        'category': np.random.choice(['A', 'B'], size=size)
    })
    return data


def main() -> None:
    # Generate some dummy data
    data = generate_data()

    """
    Histogram
    Displays frequencies or ratios within the distribution of 
    one or multiple variables.
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(data['x'], kde=False, bins=20)
    plt.title('Histogram: Distribution of X')
    plt.savefig("plots/histogram.png")

    """
    KDE Plot
    Shows a kernel density estimation of a distribution.
    """
    plt.figure(figsize=(10, 6))
    sns.kdeplot(data['x'], fill=True)
    plt.title('KDE Plot: Distribution of X')
    plt.savefig("plots/kdeplot.png")

    """
    Histogram with KDE
    The histogram function also allows us to plot the kernel density 
    estimate on top of the histogram.
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(data['x'], kde=True, bins=20)
    plt.title('Histogram with KDE: Distribution of X')
    plt.savefig("plots/histogram_kde.png")

    """
    ECDF Plot
    """
    plt.figure(figsize=(10, 6))
    sns.ecdfplot(data['x'])
    plt.title('ECDF Plot: Distribution of X')
    plt.savefig("plots/ecdfplot.png")

    """
    KDE Plot
    Shows a kernel density estimation of multiple distributions in one plot.
    """
    plt.figure(figsize=(10, 6))
    sns.kdeplot(data=data, x='x', hue='category', fill=True)
    plt.title('KDE Plot: Distribution of X by Category')
    plt.savefig("plots/kdeplot_category.png")


if __name__ == "__main__":
    main()
