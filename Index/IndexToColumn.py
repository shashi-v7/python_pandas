# convert index of a given dataframe into a column

import pandas as pd

data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
df = df.reset_index()
print("\nDataFrame with Index as a Column:")
print(df)