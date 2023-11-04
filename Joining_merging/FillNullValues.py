# Combine two DataFrame objects by filling null values in one DataFrame with non-null values from other DataFrame

import pandas as pd

d1 = pd.DataFrame({
    'A': [1, 2, None, 4, None],
    'B': [None, 5, 6, None, 8],
})
d2 = pd.DataFrame({
    'A': [10, 20, 30, 40, 50],
    'B': [100, 200, 300, 400, 500],
})
df = d1.combine_first(d2)
print(df)