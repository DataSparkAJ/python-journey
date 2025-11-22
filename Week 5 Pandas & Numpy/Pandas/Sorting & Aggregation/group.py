# sorting data
# sorting data 1 column sort_values()
# df.sort_values(by='Column Name',ascending = True/False, inplace = True)

import pandas as pd

data = {'Name': ['Arun','Kartik','Priyank','Anmol','Vipin','Sumit'],
        'Salary': [10000,15000,20000,32000,12000,18000],
        'Age': [35,29,24,23,22,24]}

df = pd.DataFrame(data)
grouped = df.groupby('Age')['Salary'].sum()
print(grouped)