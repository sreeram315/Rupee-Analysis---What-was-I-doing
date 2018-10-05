import pandas as pd



df = pd.DataFrame( columns = ['RegNo','Name','DOB','CGPA','Address','Section','Contact','Batch','Department'])

#df = df.append({'RegNo': '11610529', 'Name': 'Sreeram Maram', 'DOB': '31 may 1999', 'CGPA': '8.47', 'Address': 'Hyderabad', 'Section': 'E1601', 'Contact':'8919937557', 'Department': 'ECE'}, ignore_index = True)


file_list = ['0kto2K_girls_data.txt', '2kto3K_girls_data.txt', '3kto4K_girls_data.txt', '4kto5K_girls_data.txt', '5kto6K_girls_data.txt', '6kto9K_girls_data.txt', '9kto12K_girls_data.txt', '12kto15K_girls_data.txt', '15kto16K_girls_data.txt', '16ktoend_girls_data.txt']

for file in file_list:
	print('Parsing file',file)
	handle = open(file)
	lines = handle.readlines()
	for line in lines:
		data = line.split('   ')
		#print(data[0])
		df = df.append({'RegNo': data[0], 'Name': data[1], 'DOB': data[2], 'CGPA': data[3], 'Address': data[4], 'Section': data[5], 'Contact':data[6][:-4], 'Batch': data[6][-4:], 'Department': data[7]}, ignore_index = True)
df.set_index(['RegNo'], inplace = True)
df.to_csv('all_girls_in_lpu.csv')
print(df)