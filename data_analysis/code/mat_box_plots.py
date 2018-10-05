import pandas as pd
import numpy as np
from time import sleep
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

df = pd.DataFrame({'Normal': np.random.normal(loc=1.0, scale=1.0, size=10),
					'Random': np.random.random(size = 10),
					'Gamma': np.random.gamma(2, size = 10)})

plt.figure()

print(df['Gamma'])

plt.boxplot(df['Gamma'], whis = 'range')
plt.show()