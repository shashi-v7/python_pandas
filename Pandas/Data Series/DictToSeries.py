# Write a Pandas program to convert a dictionary to a Pandas series

import pandas as pd

data = {
  'a': 100,
  'b': 200,
  'c': 300,
  'd': 400,
  'e': 800
}
df = pd.Series(data)
print(df)
