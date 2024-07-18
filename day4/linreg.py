"""
linreg.py

In this example, we will be building a linear regression model for the MPG dataset.
This dataset contains rows of cars, all with their own properties. We will apply linear
regression to try and predict the miles per gallon (MPG).
"""
# Imports
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
pd.set_option('display.max_columns', None)

# Configuration for this dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data"
column_names = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year", "origin",
                "car_name"]

# Reading the dataset into a Pandas DataFrame
auto_mpg = pd.read_csv(url, sep="\s+", names=column_names)

# Remove the missing horsepower for now
cleaned = auto_mpg[auto_mpg['horsepower'] != "?"].copy()
#missing = auto_mpg[auto_mpg['horsepower'] == "?"]

# Convert horsepower column to float
cleaned['horsepower'] = cleaned.horsepower.astype(float)

# Defining the feature columns to include
feature_cols = ['cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model_year']

# Select the relevant columns for the Linear Regression
X = cleaned.loc[:, feature_cols]
y = cleaned['mpg']

# Instantiate the model
linreg = LinearRegression()

# Fit the model
linreg.fit(X, y)

# Print the score and the coefficients
print(linreg.score(X, y))
print(linreg.coef_)

# Plotting
plt.figure(figsize=(10, 6))
sns.heatmap([linreg.coef_], cmap='viridis', xticklabels=feature_cols)
plt.title('Heatmap: Matrix Data')
plt.show()
