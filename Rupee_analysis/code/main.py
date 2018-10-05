import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt 
from time import sleep
import numpy as np 
from matplotlib.widgets import Slider, Button
import seaborn as sns
global display_string


display_string = 'Select any year to view data'

def onclick(event):
	#print('on click called')
	update(event.xdata, oc = 1)
	return
	
	year = int(event.xdata)
	if year < 1974: return
	global y_line
	global ax
	y_line.remove()
	y_line = ax.axvline(x = event.xdata, linewidth = 0.4, color = 'red')
	usd = (str(float(df[df['Year'] == year]['USD (average)'])))
	pound = (str(float(df[df['Year'] == year]['Pound Sterling (average)'])))
	yen = (str(float(df[df['Year'] == year]['Japanese Yen (end year)'])))
	display_string = 		'''Year - {}\n\n1 USD = {}\n1 Pound = {}\n1 Yen = {}\n(in Rupees)'''.format(str(year), usd, pound, yen)
	#print(display_string)
	for t in ax.texts:
		t.set_visible(False)
	ax.text(0.15, 0.7, display_string, transform=ax.transAxes, fontsize=14,verticalalignment='top')

def update(val, oc = 0):
	#print('update called')
	year = int(sldr.val)
	if oc == 1: year = int(val)
	if year < 1974: return
	global y_line
	y_line.remove()
	y_line = ax.axvline(x = sldr.val, linewidth = 0.4, color = 'red')
	usd = (str(float(df[df['Year'] == year]['USD (average)'])))
	pound = (str(float(df[df['Year'] == year]['Pound Sterling (average)'])))
	yen = (str(float(df[df['Year'] == year]['Japanese Yen (end year)'])))
	display_string = 		'''Year - {}\n\n1 USD = {}\n1 Pound = {}\n1 Yen = {}\n(in Rupees)'''.format(str(year), usd, pound, yen)
	#print(display_string)
	for t in ax.texts:
		t.set_visible(False)
	ax.text(0.15, 0.7, display_string, transform=ax.transAxes, fontsize=14,verticalalignment='top')


sns.set(style="darkgrid")
df = pd.read_csv('rupee_main_file.csv')

fig, ax = plt.subplots()
plt.subplots_adjust(bottom = 0.5)

ax.plot(df['Year'], df['Pound Sterling (average)'])
ax.plot(df['Year'], df['Japanese Yen (end year)'])
ax.plot(df['Year'], df['USD (average)'])
ax.text(0.15, 0.7, display_string, transform=ax.transAxes, fontsize=12, fontname="Times New Roman",
        verticalalignment='top')
y_line = ax.axvline(x = 1975, linewidth = 0.4, color = 'red')
#ax.grid(color='powderblue', linestyle='-', linewidth=1)

plt.xlabel('Years 1974 - 2009')
plt.ylabel('Strenth of the currencies')
plt.title('Strengh of different currencies compared to Rupee(India) over the years',fontname="Times New Roman",fontweight="bold")
plt.legend()

start, end = 1974, 2009
ax.xaxis.set_ticks(np.arange(start, end, 2))
fig.autofmt_xdate()

freq = plt.axes([0.20, 0.05, 0.65, 0.03], facecolor = 'powderblue')
sldr = Slider(freq, 'Y - Value', 1971, 2009, valinit = 0)
sldr.on_changed(update)
fig.canvas.mpl_connect('button_press_event', onclick)
plt.xlabel('Set The Year here',fontname='Arial',fontweight="bold")
plt.show()
