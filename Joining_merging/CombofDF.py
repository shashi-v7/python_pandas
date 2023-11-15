# create a combination from two dataframes where a column id combination appears more than once in both dataframes

import pandas as pd

data1 = pd.DataFrame({
    'ID1': ['A', 'B', 'C', 'D', 'E'],
    'Value1': [1, 2, 3, 4, 5]
})
data2 = pd.DataFrame({
    'ID2': ['B', 'D', 'E', 'F', 'G'],
    'Value2': [6, 7, 8, 9, 10]
})
result = pd.merge(data1, data2, left_on='ID1', right_on='ID2', how='inner')
print(result)

