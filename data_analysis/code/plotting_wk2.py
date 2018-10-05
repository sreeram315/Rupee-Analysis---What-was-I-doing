import pandas as pd
import numpy as np
from time import sleep
import matplotlib as mpl
import matplotlib.pyplot as plt
import itertools

no_of_days_list = [0,31,59,90,120,151,181,212,243,273,304,334,365]
no_of_days_list = [int(i) for i in no_of_days_list]
days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359,360,361,362,363,364,365]
def max_and(row):
	maximum = max(df[df['Date'] == row['Date']]['Data_Value'])
	return maximum
def min_and(row):
	minimum = min(df[df['Date'] == row['Date']]['Data_Value'])
	return minimum
	
result_df = pd.DataFrame(columns = ['Day', 'Max_Temp', 'Min_Temp'])
dates_above_2015_df = pd.DataFrame(columns = ['Date', 'Max_Temp', 'Min_Temp'])
print('READING')
df = pd.read_csv('172a2fdce873f964749851f7565d3b3b189fad6bce734e5a5eaf082d.csv', parse_dates=[1], dayfirst=True)
#df = pd.read_csv('test_weather.csv', parse_dates=[1], dayfirst=True)
print('RED')

def get_date(row):
	if row['Date'].day == 29 and row['Date'].month == 2: return None
	#print('month=={}'.format(int(row['Date'].month)))
	return str(int(row['Date'].day) + no_of_days_list[int(row['Date'].month)-1])
def get_year(row):
	return row['Date'].year
df['Day'] = df.apply(get_date, axis = 1)
print('GOT DATE')
df['Year'] = df.apply(get_year, axis = 1)
print('GOT YEAR')
#print(df)

plotter = pd.DataFrame(columns = ['Day', 'Min_Temp', 'Max_Temp'])

scatter_this_day = []
scatter_this_temp = []

for day in days:
	print('doing now', day)
	if len(df[df['Day'] == str(day)]['Data_Value']) == 0: continue			
	max_of_this = (max(df[df['Day'] == str(day)]['Data_Value']))
	min_of_this = (min(df[df['Day'] == str(day)]['Data_Value']))
	if (int(max((df[(df['Day'] == str(day)) & (df['Data_Value'] == max_of_this)]['Year'])))) == 2015: #If the max value is from the year 2015( here 2015 is highest year so you used max() if if not use "if 2015 in {}".format(that condition) which returns a series, maybe better to convert it into a list just in case.)
		scatter_this_day.append(max(df[df['Day'] == str(day)]['Day']))
		scatter_this_temp.append(max(df[df['Day'] == str(day)]['Data_Value']))
		print('got maxiii')
		#sleep(1)
	if (int(max(df[(df['Day'] == str(day)) & (df['Data_Value'] == min_of_this)]['Year']))) == 2015:
		scatter_this_day.append(min(df[df['Day'] == str(day)]['Day']))
		scatter_this_temp.append(min(df[df['Day'] == str(day)]['Data_Value']))
		print('got minii')
		#sleep(1)
	plotter = plotter.append({'Day':str(day), 'Max_Temp':str(max_of_this), 'Min_Temp': str(min_of_this)}, ignore_index = True)
	continue
	"""
	for index, row in df.iterrows():
		print(row['Date'].day)
	print(df[df['Date'].day == 13])
	exit()
	print(df[(df['Data_Value']) == 220])
	df['Day'] = int(str(df['Date'])[8:10])
	print(df)
	exit()
	print(df[int(str(df['Date'])[8:10]) == day])
	exit()
	
	exit()
	print(df[	int(str(df['Date'])[:2]) == int(day) 	])
	exit()
	print(str(df['Date'])[:2])
	print(df[str(df['Date'])[:2] == day])
	max_of_this = max(df[str(df['Date'])[:2] == day]['Data_Value'])
	min_of_this = min(df[str(df['Date'])[:2] == day]['Data_Value'])
	print('max_of_this=={} and min_of_this=={}'.format(max_of_this, min_of_this))
	"""
#plotter.set_index(['Day'], inplace = True)
#print(plotter)




"""
date_2015 = pd.to_datetime('01-01-2015')
count = 0
d = df
for date in observation_dates:
	count += 1
	if count %100 == 0:
		print('iteration',count)
	data_f = df[df['Date'] == date]
	max_of_this = max(data_f['Data_Value'])
	min_of_this = min(data_f['Data_Value'])
	df.drop(df[(df.Date == date) & (df.Data_Value != int(min_of_this)) & (df.Data_Value != int(max_of_this))].index, inplace = True)
print('PART 1')


df.set_index(['Date'], inplace = True)


df = df.reset_index()
df['Max_Temp']= df.apply(max_and, axis = 1)
df['Min_Temp']= df.apply(min_and, axis = 1)
df = df[['Date', 'Min_Temp', 'Max_Temp']]
result_df = df
result_df = result_df.drop_duplicates(keep='first')

ddf = result_df
minimum_before_2015 = min(list(ddf[ddf['Date'] < date_2015]['Min_Temp']))
maximum_before_2015 = max(list(ddf[result_df['Date'] < date_2015]['Max_Temp']))
"""


plt.figure()




observation_days = list(plotter['Day'])
minies = list(plotter['Min_Temp'])
maxies = list(plotter['Max_Temp'])
print('PART 2')

new_x1, new_y1 = observation_days, minies
new_x2, new_y2 = observation_days, maxies


#for i in range(len(observation_days)):
#	print(observation_days[i],'---',minies[i],'----',maxies[i])


new_x1, new_y1 = list(plotter['Day']), list(plotter['Min_Temp'])
new_x2, new_y2 = list(plotter['Day']), list(plotter['Max_Temp'])
new_y1 = [float(i) for i in new_y1]
new_y2 = [float(i) for i in new_y2]
plt.plot(new_x1, new_y1,'-', c='blue')
plt.plot(new_x2, new_y2, '-', c='red')
fig, ax = plt.subplots()
ax.plot(new_x1,new_y1)
ax.plot(new_x1,new_y2,c='r')
start, end = ax.get_xlim()
ax.xaxis.set_ticks(np.arange(start, end, 15))

plt.fill_between(new_x1, new_y1, new_y2, facecolor = 'blue', alpha = 0.25)
plt.xlabel('Days of an year')
plt.ylabel('Temperature')
plt.title('Temperature over the years 2005-2015 in the USA')
print('PART 3')

"""
scatter_this_date = []
scatter_this_temp = []
print('these are minies')
result_df.to_csv('result_df.csv')
result_df = result_df.reset_index()
dates_above_2015_df = result_df[result_df['Date'] >= date_2015]
dates_above_2015_df.to_csv('dates_above_2015_df.csv')
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
"""
plt.scatter(scatter_this_day, scatter_this_temp, s=50, c='r', label = 'Record Breakers')
plt.legend()
plt.legend(['Min Temperature','Max Temperature','Range of Temperature', 'Record Breakers of 2015'])
print('DONE DOANNDON DONE')
plt.show()












#observation_dates = np.arange('2017-01-01', dtype = 'datetime64[D]')
##observation_dates = list(map(pd.to_datetime, observation_dates))
#print('DONE')