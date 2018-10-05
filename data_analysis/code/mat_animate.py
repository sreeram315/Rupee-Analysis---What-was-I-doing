import pandas as pd
import numpy as np
from time import sleep
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animate

n = 100
X = np.random.randn(n)

def update(curr):
	if curr == n:
		a.event_source.stop()
	plt.cla()
	bins = np.arange(-4, 4, 0.5)
	plt.hist(X[:curr], bins = bins)
	plt.axis([-4,4,0,30])
	plt.annotate('n = {}'.format(curr), [3, 27])

fig = plt.figure()
a = animate.FuncAnimation(fig, update, interval = 1)
plt.show()