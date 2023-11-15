import pandas as pd
import numpy as np

# Create a time-series with two index labels and random values
index_labels = pd.MultiIndex.from_product([['Label1', 'Label2'], 
                                           pd.date_range('2022-01-01', periods=5)], 
                                           names=['Label', 'Date'])
time_series_data = np.random.rand(10)

time_series = pd.Series(time_series_data, index=index_labels)

# Print the type of the index
print("Time-series with two index labels and random values:")
print(time_series)
print("\nType of the index:", type(time_series.index))