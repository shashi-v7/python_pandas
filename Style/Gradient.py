import pandas as pd
import numpy as np

np.random.seed(42)
data = np.random.rand(10, 4)
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])
def gradient_color(val):
    color = f'rgb({int(val*255)}, {int((1-val)*255)}, 150)'
    return f'background-color: {color}'
styled = df.style.applymap(gradient_color)
styled