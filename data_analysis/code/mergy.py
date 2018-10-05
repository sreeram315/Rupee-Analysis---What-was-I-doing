import pandas as pd
import numpy as np
import re

def answer_one():
    def pent_to_gig(string):
        if type(string) == int :
            return string * 1000000
        else:
            return np.nan
    def lookup(string):
        dic={"Republic of Korea": "South Korea",
               "United States of America": "United States",
               "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
               "China, Hong Kong Special Administrative Region": "Hong Kong"}
        if string in dic:
            return dic[string]
        return string
    
    def lookup2(string):
        dic={"Korea, Rep.": "South Korea", 
               "Iran, Islamic Rep.": "Iran",
               "Hong Kong SAR, China": "Hong Kong"}
        if string in dic:
            return dic[string]
        return string
    
    def remove_Pars(string):
        if '(' in string:
            i = string.index('(') - 1
            return string[:i]
        else:
            return string
            
    def remove_Nums(string):
        return re.sub("\d+", "",string)

    def app_int(row):
        return float(row['Energy Supply per Capita'])

    def energ():
        energy =  pd.read_excel('Energy Indicators.xls', header=17, skip_footer=38, parse_cols='C:F') 
        names=['Energy Supply', 'Energy Supply per Capita', '% Renewable']
        energy.columns = names
        energy.index.names = ['Country']
        energy.reset_index(inplace = True)
        
        energy['Country'] = energy['Country'].apply(remove_Nums, axis=1)
        energy['Energy Supply'] =  energy['Energy Supply'].apply(pent_to_gig, axis=1)
       
        
        energy['Country'] = energy['Country'].apply(lookup)
        energy['Country'] = energy['Country'].apply(remove_Pars, axis=1)
        return energy

    def ggDP():
        GDP = pd.read_csv('world_bank.csv', header=4)
        GDP['Country Name'] = GDP['Country Name'].apply(lookup2)
        GDP = GDP.rename(columns = {'Country Name':'Country'})
        GDP = GDP[['Country', '2006', '2007', '2008','2009','2010', '2011','2012','2013','2014','2015']]
        return GDP

    def Schim():
        ScimEn =  pd.read_excel('scimagojr-3.xlsx',passe_cols='A:H') 
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

    
    
    return merger

print(answer_one())