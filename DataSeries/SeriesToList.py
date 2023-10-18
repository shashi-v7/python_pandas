# Write a Pandas program to convert a Panda module Series to Python list and it's type

import pandas as pd

data = pd.Series([1, 2, 3, 4, 5])
my_list = data.tolist()
list_type = type(my_list)
print(my_list)
print(list_type)
