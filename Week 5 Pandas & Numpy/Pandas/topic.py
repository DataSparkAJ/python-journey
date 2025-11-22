'''
1- how big is your data
2- what are the names of columns
'''

import pandas as pd

data = {"Name": ['Ajay', 'Amit', 'Rohit', 'Himanshu', 'Ravi', 'Harsh'],
        "Age": [20,21,22,23,24,25],
        "Salary": [20000, 25000, 30000, 35000, 40000, 45000],
        "Performance Score": [90,89,88,87,86,85]}
df = pd.DataFrame(data)
print("Sample Dataframe: ")
print(df)

print("Shape: ", df.shape)
print("Column Names: ", df.columns)