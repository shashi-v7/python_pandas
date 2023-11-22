import pandas as pd
import numpy as np

np.random.seed(42)
data = np.random.rand(10,4)
df = pd.DataFrame(data, columns = ['A', 'B', 'C', 'D'])
def style_cells(s):
    is_max = s == s.max()
    return ['background-color: black; color: yellow' if v else '' for v in is_max]
style = df.style.apply(style_cells)
style