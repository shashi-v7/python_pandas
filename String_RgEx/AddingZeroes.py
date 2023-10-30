# add leading zeros to the integer column in a pandas series and makes the length of the field to 8 digit

import pandas as pd

data = data = {
    'ID': [123, 4567, 89012, 345678],
}
series = pd.Series(data['ID'])
series_with_zeroes = series.astype(str).str.zfill(8)
df = pd.DataFrame({'Original': series, 'Adding Zeroes': series_with_zeroes})
print(df)