import pandas as pd
from scipy import stats
import warnings
warnings.filterwarnings('ignore')
global states
states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}

def get_list_of_university_towns():
    dic = {}
    handle = open('university_towns.txt')
    lines = handle.readlines()
    for word in lines:
        word = word.rstrip()
        if 'edit' in word:
            dic[word[:word.index('[')]] = []
            pres_state = word[:word.index('[')]
        else:
            if '(' in word:
                dic[pres_state].append(word[:word.index('(')-1])
            else:
            	dic[pres_state].append(word)

    df = pd.DataFrame()
    for key, values in dic.items():
        for value in list(values):
            df = df.append({'State': key, 'RegionName': value}, ignore_index = True)
    df = df[['State', 'RegionName']]
    return df
def get_recession_start():
    '''Returns the year and quarter of the recession start time as a 
    string value in a format such as 2005q3'''
    def find_res_gdp():
        for i in range(1,len(gdp)):
            if gdp[i] < gdp[i-1] and gdp[i+1] < gdp[i]:
                ans = gdp[i]
                i += 2
                while gdp[i+1] < gdp[i]: i += 1
                if gdp[i+1] > gdp[i]:
                    return ans
                else:
                    continue


    file = pd.read_excel('gdplev.xls',header = 219, parse_cols = 'E:G', names = ['Quarter', 'Pres_doll', '2009_doll'])
    gdp = list(file['2009_doll'])
    file.set_index('Quarter', inplace = True)
    return file.index[file['2009_doll'] == find_res_gdp()][0]
def get_recession_end():
    def find_res_gdp():
        for i in range(1,len(gdp)):
            if gdp[i] < gdp[i-1] and gdp[i+1] < gdp[i]:
                ans = gdp[i]
                i += 2
                while gdp[i+1] < gdp[i]: i += 1
                if gdp[i+1] > gdp[i]:
                    return gdp[i+2]
                else:
                    continue


    file = pd.read_excel('gdplev.xls',header = 219, parse_cols = 'E:G', names = ['Quarter', 'Pres_doll', '2009_doll'])
    gdp = list(file['2009_doll'])
    file.set_index('Quarter', inplace = True)
    return file.index[file['2009_doll'] == find_res_gdp()][0]
def get_recession_bottom():
    def find_res_gdp():
        for i in range(1,len(gdp)):
            if gdp[i] < gdp[i-1] and gdp[i+1] < gdp[i]:
                ans_ind = i
                ans = gdp[i]
                i += 2
                while gdp[i+1] < gdp[i]:
                    i += 1
                    end_ind = i+2
                return min(gdp[ans_ind:end_ind])


    file = pd.read_excel('gdplev.xls',header = 219, parse_cols = 'E:G', names = ['Quarter', 'Pres_doll', '2009_doll'])
    gdp = list(file['2009_doll'])
    file.set_index('Quarter', inplace = True)
    return file.index[file['2009_doll'] == find_res_gdp()][0]
def convert_housing_data_to_quarters():
    data = pd.read_csv('City_Zhvi_AllHomes.csv')
    data = data.drop(['RegionID', 'Metro','CountyName', 'SizeRank'], axis =  1)
    df = data[['State', 'RegionName']]

    for i in range(2000, 2017):
        try:
            df[str(i) + 'q1'] = (data[str(i) + '-01'] + data[str(i) + '-02'] + data[str(i) + '-03'])/3
        except:
            c = 0
        try:
            df[str(i) + 'q2'] = (data[str(i) + '-04'] + data[str(i) + '-05'] + data[str(i) + '-06'])/3
        except:
            c = 0
        try:
            df[str(i) + 'q3'] = (data[str(i) + '-07'] + data[str(i) + '-08'] + data[str(i) + '-09'])/3
        except:
            if str(i) + '-09' not in list(data.columns): data[str(i) + '-09'] = 0
            df[str(i) + 'q3'] = (data[str(i) + '-07'] + data[str(i) + '-08'] + data[str(i) + '-09'])/3
        try:
            df[str(i) + 'q4'] = (data[str(i) + '-10'] + data[str(i) + '-11'] + data[str(i) + '-12'])/3
        except:
            continue
    df = df.replace({'State': states})
    df.set_index(['State', 'RegionName'], inplace = True)
    df.sort_values('State', inplace = True)
    df.to_csv('abc.csv')
    return df


def run_ttest():
    house_pricing = convert_housing_data_to_quarters()
    hous_pricing = house_pricing.iloc[:,list(house_pricing.columns).index(get_recession_start()):list(house_pricing.columns).index(get_recession_bottom())+1].copy()
    hous_pricing['Ratio'] = house_pricing['2008q2']/house_pricing[get_recession_bottom()]
    uni_towns = get_list_of_university_towns()
    uni_towns['University'] = True
    uni_towns.set_index(['State', 'RegionName'], inplace = True)
    uni_towns = uni_towns.merge(hous_pricing, left_index=True, right_index=True, how='right')
    sub1 = uni_towns[uni_towns['University'] == True]
    sub2 = uni_towns[uni_towns['University'] != True]
    print(list(stats.ttest_ind(sub1['Ratio'], sub2['Ratio'], nan_policy='omit')))



run_ttest()



