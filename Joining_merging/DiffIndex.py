# combine the columns of two potentially differently-indexed DataFrames into a single result DataFrame

import pandas as pd


index1 = ['row1', 'row2', 'row3']
index2 = ['row2', 'row3', 'row4']

data1 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
}, index = index1)
data2 = pd.DataFrame({
    'C': [7, 8, 9],
    'D': [10, 11, 12],
}, index = index2)

result = pd.concat([data1, data2], axis=1, join='outer')
print(result)