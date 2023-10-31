# convert a specified character column in upper/lower cases in a given DataFrame.

import pandas as pd

data = {
    'Text': ['apple', 'banana', 'cherry', 'date', 'fig'],
}
df = pd.DataFrame(data)
specified_column = 'Text'
df[specified_column] = df[specified_column].str.upper()
# df[specified_column] = df[specified_column].str.lower()
print(df)