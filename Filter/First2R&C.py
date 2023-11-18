import pandas as pd

data = {
    'Year': [1986, 1986, 1985, 1986, 1987],
    'WHO region': ['Western Pacific', 'Americas', 'Africa', 'Americas', 'Americas'],
    'Country': ['Viet Nam', 'Uruguay', "Cte d'Ivoire", 'Colombia', 'Saint Kitts and Nevis'],
    'Beverage Types': ['Wine', 'Other', 'Wine', 'Beer', 'Beer'],
    'Display Value': [0.00, 0.50, 1.62, 4.27, 1.98]
}
df = pd.DataFrame(data)
first_2_rows = df.head(2)
first_2_cols = df.iloc[:, :2]
specific_cols = df[['Country', 'Beverage Types']]
print('First 2 Rows:')
print(first_2_rows)
print('\n First 2 Columns:')
print(first_2_cols)
print('\n Specific Cols')
print(specific_cols)