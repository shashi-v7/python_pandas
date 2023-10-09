# Write a Pandas program to create and display a one-dimensional array-like object containing an array of data using Pandas module

import pandas as pd

data = ['Shashi', 'Shiva', 'Charan']
df = pd.Series(data)
print(df)