import pandas as pd
import numpy as np

np.random.seed(42)
data = np.random.rand(10, 4)
df = pd.DataFrame(data, columns = ['A', 'B', 'C', 'D'])
style = df.style.highlight_max(color = 'red')
style