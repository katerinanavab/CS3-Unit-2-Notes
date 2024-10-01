# importing libraries "as" alias
import numpy as np
import pandas as pd

# *** Pandas SERIES Object ***
# Series are 1D arrays of indexed data

# Create Series from a list/array
data = pd.Series([0.25, 0.5, 0.75, 1.0])
print(data.values) # looks like a list
print(data.index) # range computed for indices
# Access Series data by index
print("Getting one value from Series:", data[1])
print("Getting multiple values will also show indices and data type:")
print(data[0:3]) # not including stop index

# Series are like arrays but with EXPLICIT indexing
grades = pd.Series([9, 10, 11, 12], index=['freshman','sophomore','junior','senior'])
print(grades)
# Access Series data by index
print("Seniors are in grade ", grades['senior'])

# Can also create a Series from a dictionary
cookies_dict = { 'double chocolate': 5,
                'chocolate chip': 8.5,
                'oatmeal raisin': 9,
                'snickerdoodle': 10,
                'dirt': 1 }
cookies = pd.Series(cookies_dict)
print(cookies) # Dict keys become indices of the Series
# Access item by index
print("Rating of dirt cookies: ", cookies['dirt'])


# DataFrame is like a 2D array or specialized dictionary
cookies_df = pd.DataFrame(cookies, columns=['rating'])
print(cookies_df)

# Add a column to our DataFrame
cookies_df['allergens'] = [True, True, True, True, False]
print(cookies_df)

# Another way to add a column, specifying keys
cookies_df['sweetness'] = { 'double chocolate': 10,
                'oatmeal raisin': 7,
                'snickerdoodle': 8,
                'dirt': -1}
print(cookies_df)

# *** DATA SELECTION ***
data = pd.Series(['a', 'c', 'e'], index=[1, 3, 5])

# Indexing uses the explicit index
print(data[3])

# Slicing (getting multiple values) uses IMPLICIT index
print(data[3:5]) # not getting expected output

# Instead, use the LOC attribute to get a slice that uses explicit indices
print(data.loc[3:5]) # includes item at index 5 too!

# Not as common, iLOC uses implicit indices
print(data.iloc[0:1]) # doesn't include second item



