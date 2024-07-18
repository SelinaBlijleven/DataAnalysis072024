"""
pairwise_plots.py

Pairwise plots are useful for visualizing relationships between pairs of variables in a dataset.
"""
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    # Pairplot
    plt.figure(figsize=(10, 10))
    sns.pairplot(sns.load_dataset("penguins"), hue='species')
    plt.title('Pairwise Relationships in the Dataset')
    plt.savefig("plots/pairplot.png")


if __name__ == "__main__":
    main()
