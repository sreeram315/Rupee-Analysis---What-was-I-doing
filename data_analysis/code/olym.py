import pandas as pd


def answer_one():
    df.set_index('Gold')
    df.sort_index()
    return df.iloc[0]


df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index) 
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)



#df = df.drop('Totals')
#df['xxxx']=(df['Gold']-df['Gold.1'])
#print(df)

#answer0
#print(df.iloc[0])
#answer1

#ans=list(df.index[df['Gold']==max(df['Gold'])])
#print(ans[0])


#answer2
#print(df)
#print(max(df['Gold']-df['Gold.1']))
#ans=list(df.index[(df['Gold']-df['Gold.1'])==max(df['Gold']-df['Gold.1'])])
#print(df.loc['Norway','xxxx'])
#print(ans)
#exit()

#answer3
#d=df
#d=d[d.Gold>=1]
#d=d[d['Gold.1']>=1]


#ans=list(		d.index[((d['Gold']-d['Gold.1'])/(d['Gold.2']))		==		(max((d['Gold']-d['Gold.1'])/(d['Gold.2'])))]		)
#print(ans[0])
#exit()
#answer4
c=df.copy()
c['points']=(c['Gold.2'])*3 + (c['Bronze.2'])*1 + (c['Silver.2'])*2
print(c['points'])
print(len(c['points']))
#answer5
























#print(c)
#print((df['Gold']>=1) & (df['Gold.1']>=1) & max((df['Gold']-df['Gold.1'])/(df['Gold']-df['Gold.1']) ))
#print(max((df['Gold']-df['Gold.1'])/(df['Gold']+df['Gold.1'])))
#print(df.loc[(df['Gold']-df['Gold.1'])==max(df['Gold']-df['Gold.1'])])








#print(df.iloc[1])

#print(max(df['Gold']))