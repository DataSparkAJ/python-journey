import pandas as pd

data = {"Name": ['Ajay','Abhilash', 'Amit', 'Rohit', 'Himanshu', 'Ravi', 'Harsh'],
        "Age": [20,None,21,22,23,24,25],
        "Salary": [20000, None, 25000, 30000, 35000, 40000, 45000],
        "Performance Score": [90,None,89,88,87,86,85]}
df = pd.DataFrame(data)
print(df)
# linear, polynomial, time

df.interpolate(method='linear', axis=0, inplace=True)
print(df)
