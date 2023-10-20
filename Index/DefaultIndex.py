#  Write a Pandas program to display the default index and set a column as an Index in a given dataframe.

import pandas as pd

data = {
    'ID': [101, 102, 103, 104],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 22, 35]
}
df = pd.DataFrame(data)
print(df)
df = df.set_index('ID')
print(df)
