import pandas as pd
import numpy as np
from time import sleep
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.figure()
plt.title('BIF TITLE')
data = np.array([i for i in range(10)])

ax_1 = plt.subplot(1,3,1)
plt.title('Small title 1')
plt.plot(data, '-o')
ax_2 = plt.subplot(1,3,3, sharey = ax_1)
plt.plot(np.array([i**2 for i in range(10)]), '-o')
plt.title('Small title 2')
plt.plot(data,'-o')






plt.show()