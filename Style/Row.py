import pandas as pd
import numpy as np

np.random.seed(42)
data = np.random.rand(10, 4)
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])
def highlight_row(row):
    color = 'background-color: green'
    return [color if val > 0.5 else '' for val in row]
style = df.style.apply(highlight_row, axis = 1, subset=['B'])
style