import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)
data = np.random.rand(10, 4)
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])
plt.figure(figsize=(8,6))
sns.heatmap(df, cmap = 'YlGnBu', annot = True, fmt = '.2f', linewidths = 0.5)
plt.show()