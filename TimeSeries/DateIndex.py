import pandas as pd

date_strings = ['2022-03-15', '2022-03-16', '2022-03-17', '2022-03-18',
                '2022-03-19']
date_index = pd.to_datetime(date_strings)
time_series = pd.Series([1, 2, 3,4, 5], index = date_index)
print(time_series)