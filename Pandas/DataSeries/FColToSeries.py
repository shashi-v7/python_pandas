# Write a Pandas program to convert the first column of a DataFrame as a Series

import pandas as pd

data = {
    'col1' : ['1', '2', '3', '4', '5'],
    'col2' : ['A', 'B', 'C', 'D', 'E'],
    'col3' : ['Pass', 'Fail', 'Fail', 'Pass', 'Fail']
}
df = pd.DataFrame(data)
s1 = df.iloc[:,0]
print(s1)