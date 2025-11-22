import pandas as pd 

df_Region1 = pd.DataFrame({'Customer ID': [1,2],
                           'Name': ['Raju','Narendar']})

df_Region2 = pd.DataFrame({'Customer ID': [3,4],
                           'Name': ['Baburao','Nanne']})

df_concat = pd.concat([df_Region1,df_Region2], axis = 0, ignore_index= True)
print(df_concat)