"""
regression_plots.py

Regression plots are useful for understanding relationships between variables and fitting linear models.
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
        'category': np.random.choice(['A', 'B'], size=size)
    })
    return data


def main():
    # Generate some dummy data
    data = generate_data()

    # Regression plot
    plt.figure(figsize=(10, 6))
    sns.regplot(x='x', y='y', data=data)
    plt.title('Regression Plot: Relationship between X and Y')
    plt.savefig("plots/regplot.png")

    # LM plot
    plt.figure(figsize=(10, 6))
    sns.lmplot(x='x', y='y', hue='category', data=data)
    plt.title('LM Plot: Relationship between X and Y by Category')
    plt.savefig("plots/lmplot.png")

    # Residual plot
    plt.figure(figsize=(10, 6))
    sns.residplot(x='x', y='y', data=data)
    plt.title('Residual Plot: Residuals of the Linear Regression Model')
    plt.savefig("plots/residplot.png")


if __name__ == "__main__":
    main()
