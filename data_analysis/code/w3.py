import pandas as pd
import numpy as np

energy =  pd.read_excel('Energy Indicators.xls', sheet_name=0, header=17, skipfooter=38, usecols='C:F', names=['Energy Supply', 'Energy Supply per Capita', '% Renewable']) 
energy.index.rename('Country',inplace = True)
energy.reset_index(inplace = True)

def pent_to_gig(row):
	if type(row['Energy Supply']) == int:
		 return row['Energy Supply'] * 1000000
	else:
		return None

def remove_Pars(row):
	try:
		i = row['Country'].index('(') - 1
		return row['Country'][:i]
	except:
		return row['Country']

def remove_Nums(row):
	nodigits=''
	for i in row['Country']:
		if not i.isdigit():
			nodigits+=i
	return nodigits

energy['Energy Supply'] =  energy.apply(pent_to_gig, axis=1)
energy['Country'] = energy.apply(remove_Pars, axis=1)
energy['Country'] = energy.apply(remove_Nums, axis=1)



energy['Country'].replace('United States of America','United States',inplace=True)
energy['Country'].replace('Republic of Korea','South Korea',inplace=True)
energy['Country'].replace('United Kingdom of Great Britain and Northern Ireland','United Kingdom',inplace=True)
energy['Country'].replace('China, Hong Kong Special Administrative Region','Hong Kong',inplace=True)



GDP = pd.read_csv('world_bank.csv', header=4)
GDP['Country Name'].replace('Korea, Rep.','South Korea',inplace=True)
GDP['Country Name'].replace('Iran, Islamic Rep.','Iran',inplace=True)
GDP['Country Name'].replace('Hong Kong SAR, China','Hong Kong',inplace=True)
GDP = GDP.rename(columns = {'Country Name':'Country'})



ScimEn =  pd.read_excel('scimagojr-3.xlsx', sheet_name=0, header=0, skipfooter=38, usecols='A:H', names=['Rank','Country','Documents','Citable documents','Citations','Self-citations','Citations per document','H index']) 

#print(energy.head(),'\n\n')
#print(GDP.head(),'\n\n')
#print(ScimEn.head())
ScimEn = ScimEn.drop(ScimEn.index[15:])

merger = energy.merge(GDP, how='outer', left_on = 'Country', right_on = 'Country')
merger = merger.merge(ScimEn, how='right',left_on = 'Country', right_on = 'Country')



merger = merger[['Country','Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']]
merger.sort_values('Rank',inplace = True)
merger.set_index(['Country'],inplace = True)
print(merger)