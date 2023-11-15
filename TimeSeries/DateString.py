import pandas as pd

date_str = "2022-03-15"
date_from_string = pd.to_datetime(date_str)
print("Date from given string format:", date_from_string)