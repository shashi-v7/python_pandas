# Write a Pandas program to check if a specified column starts with a specified string in a DataFrame.

import pandas as pd

data = {
    'Text': ['apple', 'banana', 'cherry', 'date', 'fig'],
}
df = pd.DataFrame(data)
specified_string = 'a'
df['specified_string'] = df['Text'].str.startswith(specified_string)
print(df)