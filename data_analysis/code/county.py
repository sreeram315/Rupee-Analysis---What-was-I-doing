

import pandas as pd

census_df = pd.read_csv('census.csv')



#print()

#answer5
df=census_df
df=df.groupby('STNAME')['COUNTY'].sum()
df=df.reset_index()
df.columns = df.columns.str.replace('COUNTY','NNNN')

df=df.set_index('STNAME')
#print(df)
ans=df.index[df['NNNN']==max(df['NNNN'])]
#print( ans[0])
#print(df.index[df['']==208])
#print(df['STNAME',max('COUNTY')])
#print(df.index[df['COUNTY']==max(df['COUNTY'])])
#exit()
#answer6

cols=['STNAME','CENSUS2010POP','SUMLEV']
df=census_df

df=df[cols]
df =df.set_index(['STNAME'])
#print(df)

df= df.sort_values('CENSUS2010POP',ascending=False)
#print(df['CENSUS2010POP'])
#print("is",max(df.loc['Alaska']))


count={}
pop={}

for index,row in df.iterrows():
	if (index in count) and row['SUMLEV']==50:
		if count[index]==3:
			continue
		elif count[index]<3 :
			count[index]+=1
			pop[index]+=row['CENSUS2010POP']
	elif row['SUMLEV']==50:
		count[index]=1
		pop[index]=row['CENSUS2010POP']

max_pop=0
lst=[]
print(pop)
for i in range(3):
	for key,value in pop.items():
		if value>max_pop:
			max_pop=value
			max_city=key
	lst.append(max_city)
	pop[max_city]=0
	max_pop=0
#lst.reverse()
print(lst)
exit()
#answer7

df=census_df
df=df.set_index(['CTYNAME'])
df['ABS']=0
for index, row in df.iterrows():
    df.at[index,'ABS']=(max(row['POPESTIMATE2010'],row['POPESTIMATE2011'],row['POPESTIMATE2012'],row['POPESTIMATE2013'],row['POPESTIMATE2014'],row['POPESTIMATE2015']) - min(row['POPESTIMATE2010'],row['POPESTIMATE2011'],row['POPESTIMATE2012'],row['POPESTIMATE2013'],row['POPESTIMATE2014'],row['POPESTIMATE2015']))

m=max(df['ABS'])
df=df.reset_index()
df=df[['SUMLEV','CTYNAME','ABS']]

df=df.sort_values(['ABS'])
df=df.set_index(['SUMLEV'])
df=df.drop(index=40,axis=0)

df=df.set_index(['CTYNAME'])
ans=df.index[df['ABS']==max(df['ABS'])]
print(ans[0])


exit()
#answer8
df=census_df

new_df=df[['STNAME','CTYNAME','REGION','POPESTIMATE2015','POPESTIMATE2014']]
df=new_df
df=df[df.CTYNAME=='Washington County']

df=df[df.POPESTIMATE2015 > df.POPESTIMATE2014]
df=df[df.REGION<3]
df=df.drop(['REGION','POPESTIMATE2015','POPESTIMATE2014'],axis=1)
#return df


