import pandas as pd
(((pd.read_csv('table-1.csv')).append(pd.read_csv('table-2.csv'))).append(pd.read_csv('table-3.csv'))).append(pd.read_csv('table-4.csv')).to_csv('rupee_main_file.csv')


#############################################################################

import pandas as pd

df = pd.read_csv('rupee_main_file.csv')

def fir(string):
	return string [:4]

df['Year'] = df['Year'].apply(fir)

df.to_csv('rupee_main_file.csv')