import pandas as pd
import numpy as np
from time import sleep
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

plt.figure()

X = np.random.random(size = 10000)
#Y = np.random.normal(loc = 0.0, scale = 1.0, size = 10000)
Y = np.random.gamma(2, size = 10000)

plt.hist2d(X, Y, bins = 25)
plt.show()