import pandas as pd


def get_list_of_university_towns():
    dic = {}
    handle = open('university_towns.txt')
    lines = handle.readlines()
    for word in lines:
    	if 'edit' in word:
        	dic[word[:word.index('[')]] = []
            pres_state = word[:word.index('[')]
        elif '(' in word:
            dic[pres_state].append(word[:word.index('(')-1])
        else:
            dic[pres_state].append(word)
    df = pd.DataFrame()
    for key, values in dic.items():
        for value in list(values):
            df = df.append({'State': key, 'RegionName': value}, ignore_index = True)
    df = df[['State', 'RegionName']]
    return df

print(get_list_of_university_towns())



