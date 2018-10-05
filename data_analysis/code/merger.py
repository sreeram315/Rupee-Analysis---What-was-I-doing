import pandas as pd
import numpy as np
import re

def answer_one():
    def pent_to_gig(row):
        if type(row['Energy Supply']) == int :
            return row['Energy Supply'] * 1000000
        else:
            return np.nan
        
    def remove_Pars(row):
        if '(' in row['Country']:
            i = row['Country'].index('(') - 1
            return row['Country'][:i]
        else:
            return row['Country']
            
    def remove_Nums(row):
        return re.sub("\d+", "", row['Country'])

    def app_int(row):
        return float(row['Energy Supply per Capita'])

    def energ():
        energy =  pd.read_excel('Energy Indicators.xls', sheet_name=0, header=17, skipfooter=38, usecols='C:F', names=['Energy Supply', 'Energy Supply per Capita', '% Renewable']) 
        energy.index.names = ['Country']
        energy.reset_index(inplace = True)
        
        energy['Country'] = energy.apply(remove_Nums, axis=1)
        energy['Energy Supply'] =  energy.apply(pent_to_gig, axis=1)
       
        dic={"Republic of Korea": "South Korea",
               "United States of America": "United States",
               "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
               "China, Hong Kong Special Administrative Region": "Hong Kong"}
        energy = energy.replace({'Country':dic})
        energy['Country'] = energy.apply(remove_Pars, axis=1)
        return energy

    def ggDP():
        GDP = pd.read_csv('world_bank.csv', header=4)
        dic={"Korea, Rep.": "South Korea", 
           "Iran, Islamic Rep.": "Iran",
           "Hong Kong SAR, China": "Hong Kong"}
        GDP = GDP.replace({'Country Name':dic})
        GDP = GDP.rename(columns = {'Country Name':'Country'})
        GDP = GDP[['Country', '2006', '2007', '2008','2009','2010', '2011','2012','2013','2014','2015']]
        return GDP

    def Schim():
        ScimEn =  pd.read_excel('scimagojr-3.xlsx',usecols='A:H') 
        return ScimEn
    energy = energ()
    GDP = ggDP()
    ScimEn = Schim()
   
    energy.set_index(['Country'],inplace = True)
    GDP.set_index(['Country'],inplace=True)
    ScimEn.set_index(['Country'],inplace=True)

    merger = energy.merge(GDP, how='inner', on = 'Country')
    merger = merger.merge(ScimEn, how='inner',on = 'Country')    
  
    
    merger = merger[merger['Rank']<=15]
    merger = merger[['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']]
    
    merger.to_csv('hell.csv')
    print(merger)
    exit()
    return merger

#print(answer_one())

#answer2
 #energy_set = set(energy.index)
    #GDP_set = set(GDP.index)
    #ScimEn_set = set(ScimEn.index)

    #o = energy_set & GDP_set & ScimEn_set
    #i = energy_set | GDP_set | ScimEn_set

    #print(len(o)-len(i))


Top15 = answer_one()



#answer3

df= answer_one()


df['avGDP'] = df[['2006','2015']].mean(axis=1)

#answer4



df['GDP_change'] = df['2015'] - df['2006']

print(df.sort_values('avGDP',ascending=False))
#print(df['avGDP'].dtypes)
#print(df['GDP_change'].dtypes)

#answer5

print(np.sum(df['Energy Supply per Capita'])/15)

#answer6

df = answer_one()
print(df[df['% Renewable']==max(df['% Renewable'])])

print(df.loc['Brazil','% Renewable'])

#return ('Brazil', 69.64803)
 
#answer7

df=answer_one()

df['Ratio'] = df['Self-citations']/df['Citations']

print(df['Ratio'])

print(df[df['Ratio']==max(df['Ratio'])])
print(df.sort_values('Ratio'))

#answer8
df = answer_one()
df['pop'] = df['Energy Supply'] / df['Energy Supply per Capita']
df = df.sort_values('pop')
print(df)

#answer9


df['Citable docs per Capita'] = df['Citable documents'] / df['pop']
df['Citable docs per Capita']=np.float64(df['Citable docs per Capita'])

print(df['Citable docs per Capita'].astype('float64').corr(df['Energy Supply per Capita'].astype('float64'), method = "pearson"))

#answer10

df = answer_one()

def highre(row):
    if row['% Renewable'] > df['% Renewable'].median():
        return 1
    else:
        return 0


df['HighRenew'] = df.apply(highre, axis=1)

print(df.index)

val = [0,1,1,1,0,1,0,0,1,0,0,1,1,0,0]

ind = ['Australia', 'Brazil', 'Canada', 'China', 'France', 'Germany', 'India',
       'Iran', 'Italy', 'Japan', 'South Korea', 'Russian Federation', 'Spain',
       'United Kingdom', 'United States']

h = pd.Series(val, index=ind)
print(h)
