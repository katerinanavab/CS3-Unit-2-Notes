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



