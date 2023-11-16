import pandas as pd

date_int = pd.DataFrame({
    'year': [2022, 2023, 2021],
    'month': [3, 6, 12],
    'day': [15, 20, 8]
})
date_strg = pd.DataFrame({
    'date_str': ['2022-03-15', '2023-06-20', '2021-12-08']
})
series_int = pd.to_datetime(date_int)
series_str = pd.to_datetime(date_strg['date_str'])
print("Timestamps from integer:")
print(series_int)
print("Timestamps from Strings:")
print(series_str)