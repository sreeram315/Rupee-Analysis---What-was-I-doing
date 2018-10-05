import pandas as pd
import numpy as np
from time import sleep
import matplotlib as mpl
import matplotlib.pyplot as plt
import itertools

no_of_days_list = ['31','28','31','30','31','30','31','31','30','31','30','31']
no_of_days_list = [int(i) for i in no_of_days_list]

def max_and(row):
	maximum = max(df[df['Date'] == row['Date']]['Data_Value'])
	#print('returning', date, maximum)
	return maximum
def min_and(row):
	minimum = min(df[df['Date'] == row['Date']]['Data_Value'])
	#print('returning', date,minimum)
	return minimum
result_df = pd.DataFrame(columns = ['Date', 'Max_Temp', 'Min_Temp'])
dates_above_2015_df = pd.DataFrame(columns = ['Date', 'Max_Temp', 'Min_Temp'])
print('READING')
df = pd.read_csv('172a2fdce873f964749851f7565d3b3b189fad6bce734e5a5eaf082d.csv', parse_dates=[1], dayfirst=True)
#df = pd.read_csv('test_weather.csv', parse_dates=[1], dayfirst=True)
print('RED')
#print(df['Date'])
#print('converting to date')
#df['Date'] = pd.to_datetime(df['Date'])
#print('converted to date type')
#print(len(df['Date'].unique()))
observation_dates = list(df['Date'].unique())
date_2015 = pd.to_datetime('01-01-2015')
#print(date_2015)
#print(observation_dates[0] < date_2015)
#print(observation_dates[0] > date_2015)
#dates_above_2015 = []


#for date in observation_dates:
#	if date >= date_2015:
		#print('dropping',date)
		#observation_dates = observation_dates.drop(date)
#		dates_above_2015.append(date)

#dates_above_2015 = pd.DatetimeIndex(dates_above_2015)


count = 0
d = df
for date in observation_dates:
	count += 1
	if count %100 == 0:
		print('iteration',count)
	#print('itereation', count)
	data_f = df[df['Date'] == date]
	max_of_this = max(data_f['Data_Value'])
	min_of_this = min(data_f['Data_Value'])
	#max_of_this = max(df[df['Date'] == date]['Data_Value'])
	#min_of_this = min(df[df['Date'] == date]['Data_Value'])
	#print(min_of_this)
	#print(max_of_this)
	df.drop(df[(df.Date == date) & (df.Data_Value != int(min_of_this)) & (df.Data_Value != int(max_of_this))].index, inplace = True)

	#df = df[df['Date'] == date]
	#if date >= date_2015: continue
	#print(date)
	#max_temps =  (max(df[(df['Date'] == date) & (df['Element'] == 'TMAX')]['Data_Value']))
	#min_temps =  (min(df[(df['Date'] == date) & (df['Element'] == 'TMIN')]['Data_Value']))
	#if len(max_temps) > 0:
	#	max_on_this_date = np.mean(max_temps)
	#	#print(date,max_temps,'----',max_on_this_date)
	#else:
	#	max_on_this_date = max_on_this_date
	#if len(min_temps) > 0:
	#	min_on_this_date = np.mean(min_temps)
	#	#print(date,min_temps,'----',min_on_this_date)
	#else:
	#	min_on_this_date = min_on_this_date
	#result_df = result_df.append({'Date':date, 'Max_Temp':str(max_on_this_date),'Min_Temp':str(min_on_this_date)}, ignore_index = True)
	#count += 1
	#rint(4000 - count)
print('PART 1')


df.set_index(['Date'], inplace = True)


df = df.reset_index()
df['Max_Temp']= df.apply(max_and, axis = 1)
df['Min_Temp']= df.apply(min_and, axis = 1)
df = df[['Date', 'Min_Temp', 'Max_Temp']]
result_df = df
#result_df = pd.DataFrame(columns=[])
#result_df['Date'] = df['Date']
#result_df['Date'], result_df['TMAX'], result_df['TMIN'] = result_df.apply(max_and_min, axis = 1)
#result_df.set_index(['Date'], inplace = True)
result_df = result_df.drop_duplicates(keep='first')
#print(result_df.head(50))

ddf = result_df
minimum_before_2015 = min(list(ddf[ddf['Date'] < date_2015]['Min_Temp']))
maximum_before_2015 = max(list(ddf[result_df['Date'] < date_2015]['Max_Temp']))

plt.figure()
axes = plt.gca()


plt.gcf().autofmt_xdate()

#print(result_df.head(100))

observation_dates = list(result_df['Date'])
minies = list(result_df['Min_Temp'])
maxies = list(result_df['Max_Temp'])
print('PART 2')
#print((observation_dates))
#print((minies))
#print((maxies))
#lists = sorted(itertools.izip(*[x_es, y_es]))
#new_x, new_y = list(itertools.izip(*lists))

#new_x1, new_y1 = zip(*sorted(zip(observation_dates, minies)))
#new_x2, new_y2 = zip(*sorted(zip(observation_dates, maxies)))

new_x1, new_y1 = observation_dates, minies
new_x2, new_y2 = observation_dates, maxies
plotter = pd.DataFrame(columns = ['Date', 'Min_Temp', 'Max_Temp'])
for i in range(len(observation_dates)):
	plotter = plotter.append({'Date': observation_dates[i], 'Min_Temp':minies[i],'Max_Temp':maxies[i]}, ignore_index = True)
	#print(observation_dates[i],'-----',minies[i],'-----',maxies[i])
plotter.set_index(['Date'], inplace = True)
plotter = plotter.sort_index()
plotter = plotter.reset_index()
#print(plotter.head(50))
new_x1, new_y1 = list(plotter['Date']), list(plotter['Min_Temp'])
new_x2, new_y2 = list(plotter['Date']), list(plotter['Max_Temp'])
plt.plot(new_x1, new_y1,'-', c='blue')
plt.plot(new_x2, new_y2, '-', c='red')
print(range(len(observation_dates)))

plt.fill_between(new_x1, new_y1, new_y2, facecolor = 'blue', alpha = 0.25)
plt.xlabel('Dates from 2005 to 2015')
plt.ylabel('Temperature')
plt.title('Temperature over the years 2005-2015 in the USA')
print('PART 3')

"""
for date in dates_above_2015:
	max_of_this = max(df[df['Date'] == date]['Data_Value'])
	min_of_this = min(df[df['Date'] == date]['Data_Value'])

	max_temps =  (list(df[(df['Date'] == date) & (df['Element'] == 'TMAX')]['Data_Value']))
	min_temps =  (list(df[(df['Date'] == date) & (df['Element'] == 'TMIN')]['Data_Value']))
	if len(max_temps) > 0:
		max_on_this_date = np.mean(max_temps)
		#print(date,max_temps,'----',max_on_this_date)
	else:
		max_on_this_date = max_on_this_date
	if len(min_temps) > 0:
		min_on_this_date = np.mean(min_temps)
		#print(date,min_temps,'----',min_on_this_date)
	else:
		min_on_this_date = min_on_this_date
	dates_above_2015_df = dates_above_2015_df.append({'Date':date, 'Max_Temp':str(max_on_this_date),'Min_Temp':str(min_on_this_date)}, ignore_index = True)
"""
#dates_above_2015_df.set_index(['Date'], inplace = True)
scatter_this_date = []
scatter_this_temp = []
"""
for date in observation_dates:
	max_of_this = max(df[df['Date'] == date]['Data_Value'])
	min_of_this = min(df[df['Date'] == date]['Data_Value'])
	if min_of_this < minimum_before_2015:
		scatter_this_date.append
	if date >= date_2015: continue
	maxes = (list(df[(df['Date'] == date) & (df['Element'] == 'TMAX')]['Data_Value']))
	if len(maxes) > 0: maxies.append(max(maxes))
	mines = (list(df[(df['Date'] == date) & (df['Element'] == 'TMIN')]['Data_Value']))
	if len(mines) > 0: minies.append(min(mines))
"""

#print('these are maxies')
#print(maxies)
#sleep(2)
print('these are minies')
#print(minies)
#sleep(2)
result_df.to_csv('result_df.csv')
result_df = result_df.reset_index()
dates_above_2015_df = result_df[result_df['Date'] >= date_2015]
dates_above_2015_df.to_csv('dates_above_2015_df.csv')
#print(dates_above_2015_df)
print('mini==',minimum_before_2015)
print('maxi==',maximum_before_2015)
dates_above_2015_df.set_index(['Date'], inplace = True)
for index, row in dates_above_2015_df.iterrows():
	if float(row['Max_Temp']) > float(maximum_before_2015):
		scatter_this_date.append(index)
		scatter_this_temp.append(row['Max_Temp'])
		print('GOT ONE',row['Max_Temp'],'date==',date,'temp==',row['Max_Temp'])
		sleep(1)
	if float(row['Min_Temp']) < float(minimum_before_2015):
		scatter_this_date.append(index)
		scatter_this_temp.append(row['Min_Temp'])
		print('GOT two',row['Min_Temp'])
		sleep(1)

print('PART 4')
plt.scatter(scatter_this_date, scatter_this_temp, s=50, c='r', label = 'Record Breakers')
plt.legend()
plt.legend(['Min Temperature','Max Temperature'])
print('DONE DOANNDON DONE')
plt.show()












#observation_dates = np.arange('2017-01-01', dtype = 'datetime64[D]')
##observation_dates = list(map(pd.to_datetime, observation_dates))
#print('DONE')