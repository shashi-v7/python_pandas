import pandas as pd
import numpy as np

date_range = pd.date_range(start = '2022-01-01', end = '2023-12-31', freq = 'D')
time_series_range = np.random.rand(len(date_range))
time_series = pd.Series(time_series_range, index = date_range)
print('Time seires with time indexed data:')
print(time_series)
same_year = time_series['2022']
print('\n Dates of the Same year')
print(same_year)
selected_dates = time_series['2022-03-15':'2022-03-18']
print('\n Dates between : ')
print(selected_dates)