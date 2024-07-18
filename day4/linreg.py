"""
linreg.py

In this example, we will be building a linear regression model for the MPG dataset.
This dataset contains rows of cars, all with their own properties. We will apply linear
regression to try and predict the miles per gallon (MPG).
"""
# Imports
import pandas as pd

# Configuration for this dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data"
column_names = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year", "origin",
                "car_name"]

# Reading the dataset into a Pandas DataFrame
auto_mpg = pd.read_csv(url, sep="\s+", names=column_names)

# Display the first few rows of the dataset
print(auto_mpg.head())

# TO DO
# 1. Clean the data
# 2. Select numerical data for use in the linear regression
# 3. Univariate linear regression
# 4. (Optional) Multivariate linear regression? + plotting heatmap/weights
# 5. Data visualisation
