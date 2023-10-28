# Write a Pandas program to create a DataFrame using intervals as an index

import pandas as pd

data = [10, 20, 30, 40, 50]
intervel_index = pd.IntervalIndex.from_tuples([(0,10),(1,20),(2,30),(3,40),(4,50)])
df = pd.DataFrame(data, index = intervel_index)
print(df)