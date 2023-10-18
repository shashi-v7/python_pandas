import pandas as pd

d1 = pd.Series([2, 4, 6, 8, 10])
d2 = pd.Series([1, 3, 5, 7, 9])
print('Add:')
ds = d1+d2
print(ds)
print('Subtract:')
ds = d1-d2
print(ds)
print('Product:')
ds = d1 * d2
print(ds)
print('Division:')
ds = d1/d2
print(ds)
