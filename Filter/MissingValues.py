import pandas as pd

data = {
    'Year': [1986, 1986, 1985, 1986, 1987],
    'WHO region': ['Western Pacific', 'Americas', 'Africa', 'Americas', 'Americas'],
    'Country': ['Viet Nam', 'Uruguay', "Cte d'Ivoire", 'Colombia', 'Saint Kitts and Nevis'],
    'Beverage Types': ['Wine', 'Other', 'Wine', 'Beer', 'Beer'],
    'Display Value': [0.00, 0.50, 1.62, 4.27, 1.98]
}
df = pd.DataFrame(data)
print('Dataframe with Missing Values')
print(df)
missing_values = df.isnull()
print('\nMissing Values:')
print(missing_values)
clean_null = df.dropna()
print('\nCleaning Values')
print(clean_null)