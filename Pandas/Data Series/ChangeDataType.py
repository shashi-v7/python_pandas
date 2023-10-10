# Write a Pandas program to change the data type of given a column or a Series.

import pandas as pd

data = pd.Series(['100', '200', 'Python', '300.12', '400'])
data = data.astype(float)
print(data)
