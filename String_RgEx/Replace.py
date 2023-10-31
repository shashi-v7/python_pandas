# Write a Pandas program to replace arbitrary values with other values in a given DataFrame

import pandas as pd

data = {
    'A': [1, 2, 3, 4, 5],
    'B': ['apple', 'banana', 'cherry', 'date', 'egg'],
}
df = pd.DataFrame(data)
replacement = {'apple': 'fruit', 'banana': 'fruit', 'egg': 'protein'}
df['B'] = df['B'].replace(replacement)
print(df)