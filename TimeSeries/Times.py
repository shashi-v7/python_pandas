import pandas as pd
from datetime import datetime

# Datetime object for Jan 15 2012
date_a = pd.to_datetime('2012-01-15')
print("a) Datetime object for Jan 15 2012:", date_a)

# Specific date and time of 9:20 pm
date_b = pd.to_datetime('2012-01-15 21:20:00')
print("b) Specific date and time of 9:20 pm:", date_b)

# Local date and time
date_c = pd.to_datetime('now')
print("c) Local date and time:", date_c)

# A date without time
date_d = pd.to_datetime('today').date()
print("d) A date without time:", date_d)

# Current date
date_e = pd.to_datetime('today')
print("e) Current date:", date_e.date())

# Time from a datetime
date_f = pd.to_datetime('now').time()
print("f) Time from a datetime:", date_f)

# Current local time
date_g = datetime.now().strftime('%H:%M:%S')
print("g) Current local time:", date_g)
