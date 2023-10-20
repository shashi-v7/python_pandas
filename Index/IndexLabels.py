# create an index labels by using 64-bit integers, using floating-point numbers in a given dataframe.

import pandas as pd
import numpy as np

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
labels = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], dtype = np.float64).view(np.int64)
df.index = labels
print(df)