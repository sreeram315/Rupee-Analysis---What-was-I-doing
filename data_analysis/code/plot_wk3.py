import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from math import sqrt
from matplotlib.widgets import Slider, Button
import matplotlib.colors as mcol
import matplotlib.cm as cm

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650), 
                   np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), 
                   np.random.normal(48000,70000,3650)], 
                  index=[1992,1993,1994,1995])
years = np.arange(4)

error = [(df.loc[1992].std()/sqrt(len(df.loc[1992]))), (df.loc[1993].std()/sqrt(len(df.loc[1993]))), (df.loc[1994].std()/sqrt(len(df.loc[1994]))), (df.loc[1995].std()/sqrt(len(df.loc[1995])))]


fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
l = [((df.loc[1992]).mean()), ((df.loc[1992]).mean()), ((df.loc[1994]).mean()), ((df.loc[1995]).mean())]

###############################################################################################
cm1 = mcol.LinearSegmentedColormap.from_list("Test",["blue", "white", "red"])
cpick = cm.ScalarMappable(cmap=cm1) 
cpick.set_array([])
plt.colorbar(cpick, orientation='vertical')

def percentages(threshold):
    percentages = []
    for bar in bars:
        percentage = (bar.get_height()-threshold)/(bar.get_height())
        percentage += 0.5
        #print(percentage)
        #print(percentage)
        if percentage>1:
        	percentage = 1
        elif percentage<0:
        	percentage=0
        else:
        	percentage = percentage
        percentages.append(percentage)
    return percentages


###############################################################################################

bars = ax.bar(years, l, width = 0.7, color = 'red', edgecolor = 'black', yerr = error)

frame1 = plt.gca()
frame1.axes.get_xaxis().set_ticks([])

ax.set_xticks(years)
ax.set_xticklabels(('1992','1993','1994','1995'))
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.xlabel('Years')
plt.ylabel('Samplings')
plt.title('Success probability of Samplings')

y_value = 11111

#y_value = input('Enter preferred Y - axis value:\t')
for i, bar in enumerate(bars):
	#print(int(bar.get_height()))
	if y_value < int(bar.get_height()):
		bar.set_facecolor('red')
	else:
		bar.set_facecolor('blue')
y_line = ax.axhline(y = 0, linewidth = 1, color = 'black')
ax.axhline(y = 0, xmin=-.9, xmax=1.9, clip_on = False, color = 'black')
#ax.axvline(x = -0.5, ymin=-.1, ymax=1.1, clip_on = False)


def update(val):
	global y_line
	y_line.remove()
	y_value = sldr.val
	y_line = ax.axhline(y = y_value, linewidth = 1, color = 'black')
	#for i, bar in enumerate(bars):
	#	bar.set_facecolor()
	perc = percentages(y_value)
	for bar, p in zip(bars, perc):
		bar.set_color(cpick.to_rgba(p))

freq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor = 'blue')
sldr = Slider(freq, 'Y - Value', 0, 50000, valinit = 3)
sldr.on_changed(update)
plt.xlabel('Select Y value here', size = 20)
















plt.show()
