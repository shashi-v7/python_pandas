import pandas as pd
import numpy as np

np.random.seed(42)
data = np.random.rand(10, 4)
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])

def highlight_cols(val):
    color_mapping = {
        'B': 'background-color: green',
        'C': 'background-color: red'
    }
    return color_mapping.get(val.name, '')

style = df.style.applymap(highlight_cols)
style