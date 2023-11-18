import pandas as pd
import numpy as np

data = {
    'ord_no': [np.nan, np.nan, 70002.0, 70004.0, np.nan, 70005.0, np.nan, 70010.0, 70003.0, 70012.0, np.nan, 70013.0],
    'purch_amt': [np.nan, 270.65, 65.26, 110.50, 948.50, 2400.60, 5760.00, 1983.43, 2480.40, 250.45, 75.29, 3045.60],
    'ord_date': [np.nan, '2012-09-10', np.nan, '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'],
    'customer_id': [np.nan, 3001.0, 3001.0, 3003.0, 3002.0, 3001.0, 3001.0, 3004.0, 3003.0, 3002.0, 3001.0, 3001.0]
}
df = pd.DataFrame(data)
cols_with_missing = ['ord_no','purch_amt','ord_date','customer_id']
clean = df.dropna(subset=cols_with_missing)
print(clean)