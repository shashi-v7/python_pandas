import pandas as pd

specified_date_str = "2022-03-15"
specified_date = pd.to_datetime(specified_date_str)

day_after = specified_date + pd.DateOffset(days=1)
print("Day after the specified date:", day_after)

day_before = specified_date - pd.DateOffset(days=1)
print("Day before the specified date:", day_before)

other_date_str = "2022-03-20"
other_date = pd.to_datetime(other_date_str)

days_between = (other_date - specified_date).days
print("Days between the two specified dates:", days_between)