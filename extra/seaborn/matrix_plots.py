"""
matrix_plots.py

Matrix plots are used to visualize data in a matrix format and to show relationships between different variables.
"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def generate_matrix_data(size: int = 10) -> pd.DataFrame:
    # Generate random data
    np.random.seed(42)
    data = np.random.rand(size, size)
    return pd.DataFrame(data, columns=[f'Var{i+1}' for i in range(size)])


def main():
    # Generate some dummy data
    data = generate_matrix_data()

    """
    Heatmap
    Uses colours to illustrate the difference between different values in the grid. 
    This is often applied to something like a correlation matrix, or the trained weights of a machine learning 
    model.
    """
    plt.figure(figsize=(10, 6))
    sns.heatmap(data, annot=True, cmap='viridis')
    plt.title('Heatmap: Matrix Data')
    plt.savefig("plots/heatmap.png")

    """ 
    Clustermap
    """
    sns.clustermap(data, annot=True, cmap='viridis', figsize=(10, 10))
    plt.title('Clustermap: Matrix Data')
    plt.savefig("plots/clustermap.png")


if __name__ == "__main__":
    main()
