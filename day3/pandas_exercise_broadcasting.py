# Instructions
# -Make a string object with the value 'NL' and assign it to country.
# -Construct a dictionary with 2 key:value pairs: 'country':country and 'city':cities.
# -Construct a Pandas DataFrame from the dictionary you created and assign it to df.
# -print the DataFrame
import pandas as pd

country = "nl"
cities = ["Amsterdam", "Utrecht", "Rotterdam", "Groningen", "Leiden", "Lutjebroek"]

d: dict = {
    'country':  country,
    'city':     cities
}

df: pd.DataFrame = pd.DataFrame(d)
print(df)
