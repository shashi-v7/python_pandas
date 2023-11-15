import pandas as pd

# Specific date using timestamp
date_a = pd.Timestamp('2022-03-10')
print("a) Specific date using timestamp:", date_a)

# Date and time using timestamp
date_b = pd.Timestamp('2022-03-10 15:30:00')
print("b) Date and time using timestamp:", date_b)

# Time added to the current local date using timestamp
current_date = pd.Timestamp('now').date()
time_to_add = pd.Timedelta(hours=5, minutes=45)
date_c = current_date + time_to_add
print("c) Time added to the current local date using timestamp:", date_c)

# Current date and time using timestamp
current_date_time = pd.Timestamp('now')
print("d) Current date and time using timestamp:", current_date_time)
