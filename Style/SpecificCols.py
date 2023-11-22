import pandas as pd
import numpy as np

data = {
    'A': [1, 4, 7],
    'B': [10, 20, 30],
    'C': [100, 200, 300]
}
df = pd.DataFrame(data)
def highlight_columns(val):
    highlight_cols = ['B', 'C']
    if val in highlight_cols:
        return 'background-color: yellow'
    else:
        return ''
styled_df = df.style.applymap(highlight_columns)
styled_df