# remove whitespaces, left sided whitespaces and right sided whitespaces of the string values of a given pandas series

import pandas as pd

data = {
    'Text': ['   Hello World   ', '  Python   ', '   Data Science   '],
}
series = pd.Series(data['Text'])
no_space = series.str.replace(' ', '')
left_space = series.str.lstrip()
right_space = series.str.rstrip()
df = pd.DataFrame({'Original': series, 'No WhiteSpace': no_space, 
                  'left WhiteSpace': left_space, 
                  'right_WhiteSpace': right_space})
print(df)