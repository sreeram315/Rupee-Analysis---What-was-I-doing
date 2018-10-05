import pandas as pd
import numpy as np
from time import sleep
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

"""
## HISTOGRAM GRANULARITY INSPECTION ####
plt.figure()
fig , ((ax1,ax2), (ax3,ax4)) = plt.subplots(2,2,sharex = True)

axs = [ax1, ax2, ax3, ax4]

for n in range(len(axs)):
	size = 10**(n+1)
	sample = np.random.normal(loc = 0.0, scale = 1.0, size = size)
	axs[n].hist(sample, bins = 100)
	axs[n].set_title('PLOT {}'.format(str(n)))
plt.show()
"""
"""

plt.figure()
X = np.random.random(size = 10000)
Y = np.random.normal(loc=0.0, scale = 1.0, size = 10000)
plt.subplot(1,2,2)
plt.scatter(X, Y)
plt.subplot(1,2,1)
plt.hist(X,Y, bins = 100)
plt.show()

"""

X = np.random.random(size = 10000)
Y = np.random.normal(loc=0.0, scale = 1.0, size = 10000)

plt.figure()
gspec = gridspec.GridSpec(3, 3)

top_right = plt.subplot(gspec[0, 1:])
bottom_left = plt.subplot(gspec[1:,:1])
scatter_bottom_right = plt.subplot(gspec[1:, 1:])


top_right.hist(X, bins = 100, density = True, color = 'green') 
bottom_left.hist(Y, orientation = 'horizontal', bins = 100, color = 'r', density = True)
scatter_bottom_right.scatter(X, Y)

for axis in [top_right, scatter_bottom_right]:
	axis.set_xlim(0,1)
for axis in [bottom_left, scatter_bottom_right]:
	axis.set_ylim(-4, 4)

bottom_left.invert_xaxis()
plt.show()












