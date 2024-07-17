"""
Working with the Series in Pandas.
"""
import numpy as np
import pandas as pd

# Set the filename
file = 'AAPL.csv'

# Read from the comma separated-file
aapl = pd.read_csv(file)

# Select a column
low = aapl['Low']
print(type(low))    # pd.Series

# Select the head of the table (5 lines by default)
print(low.head())

# Get a list of the values
lows = low.values
print(type(lows))   # np.ndarray
print(lows)         # values

# Select from the dataframe where a certain criterium is met
selection: pd.DataFrame = aapl.loc[aapl['Low'] > 110]
print(selection)
print(aapl.shape)
print(selection.shape)

# NumPy method for creating a column with True/False for the low-value being over 110
#aapl['isHigher'] = np.where(aapl['Low'] > 110, True, False)

# Pandas method: creating a new column based on boolean logic
aapl['isHigher'] = aapl['Low'] > 110

# We should be able to see the new column in the info
print(aapl.info())

# We can plot any column as a line plot with the following syntax.
# The same can be applied for other types of plots.
import matplotlib.pyplot as plt

plt.plot(aapl['Low'])
plt.show()