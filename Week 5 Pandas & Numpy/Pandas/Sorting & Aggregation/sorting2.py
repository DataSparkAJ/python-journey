# sorting data
# sorting data 1 column sort_values()
# df.sort_values(by='Column Name',ascending = True/False, inplace = True)

import pandas as pd

data = {'Name': ['Arun','Kartik','Priyank'],
        'Salary': [10000,15000,20000],
        'Age': [35,29,24]}

df = pd.DataFrame(data)
print(df)

sorted_values = df.sort_values(by= ['Salary','Age'], ascending= [False,True], inplace = True)
print(df)