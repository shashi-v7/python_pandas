# Write a Pandas program to convert a NumPy array to a Pandas series

import pandas as pd
import numpy as np

data = np.array([10, 20, 30, 40, 50])
df = pd.Series(data)
print(df)
