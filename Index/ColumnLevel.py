# Pandas program to convert 1st and 3rd levels in the index into columns from a multiple level of index frame of a given dataframe.

import pandas as pd

data = {
    'ID': ['s001', 's002', 's003', 's001', 's002', 's004'],
    'Class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'Name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'DOB': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'],
    'Age': [35, 32, 33, 30, 31, 32],
    'Address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4'],
    'Tag': ['t1', 't2', 't3', 't4', 't5', 't6']
}
df = pd.DataFrame(data)
df = df.set_index(['ID', 'Class', 'Name'])
print("Original DataFrame with Multi-level Index:")
print(df)
df = df.reset_index(level=[0, 2])
print("\nDataFrame with 1st and 3rd Levels as Columns:")
print(df)
