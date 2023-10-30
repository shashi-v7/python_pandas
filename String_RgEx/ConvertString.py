# Pandas program to convert all the string values to upper, lower cases in a given pandas series. Also find the length of the string values.

import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
}
df = pd.DataFrame(data)
df['Upper'] = df['Name'].str.upper()
df['Lower'] = df['Name'].str.lower()
df['Length'] = df['Name'].str.len()
print(df)