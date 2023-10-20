# Write a Pandas program to convert a given Series to an array.

import pandas as pd
import numpy as np

data = pd.Series([10, 20, 30, 40, 50])
array_data = data.to_numpy()
print(array_data)