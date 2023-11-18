import pandas as pd
import numpy as np

data = {
    'ord_no': [70001.0, np.nan, 70002.0, 70004.0, np.nan, 70005.0, np.nan, 70010.0, 70003.0, 70012.0, np.nan, 70013.0],
    'purch_amt': [150.50, np.nan, 65.26, 110.50, 948.50, np.nan, 5760.00, 1983.43, np.nan, 250.45, 75.29, 3045.60],
    'sale_amt': [10.50, 20.65, np.nan, 11.50, 98.50, np.nan, 57.00, 19.43, np.nan, 25.45, 75.29, 35.60],
    'ord_date': ['2012-10-05', '2012-09-10', np.nan, '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'],
    'customer_id': [3002, 3001, 3001, 3003, 3002, 3001, 3001, 3004, 3003, 3002, 3001, 3001],
    'salesman_id': [5002.0, 5003.0, 5001.0, np.nan, 5002.0, 5001.0, 5001.0, np.nan, 5003.0, 5002.0, 5003.0, np.nan]
}
df = pd.DataFrame(data)
columns_to_fill = ['ord_no', 'purch_amt', 'sale_amt', 'salesman_id']
df[columns_to_fill] = df[columns_to_fill].apply(lambda x: x.fillna(x.mean()))
print(df)