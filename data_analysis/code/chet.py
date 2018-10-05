

import pandas as pd
import numpy as np
import re

df = pd.read_csv('hell.csv')
df = df.reset_index()


print(df.columns)

for index,row in df.iterrows():
	print(row['2015'],',',end='')




