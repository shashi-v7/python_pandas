# join the two dataframes with matching records from both sides where available.

import pandas as pd
data1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
    'key': ['K0', 'K1', 'K2', 'K3']
})
data2 = pd.DataFrame({
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3'],
    'key': ['K0', 'K1', 'K2', 'K4']
})
result = pd.merge(dataframe1, dataframe2, on='key', how='outer')
print(result)
