import pandas as pd

epoch_time = 1609459200
timestamp_utc = pd.to_datetime(epoch_time, unit = 's', utc = True)
print('Timestamp in UTC', timestamp_utc)
desired_timezone = 'America/New_York'
timestamp = timestamp_utc.tz_convert(desired_timezone)
print('Timestamp in', desired_timezone, ':', timestamp)