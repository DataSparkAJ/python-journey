import pandas as pd

data = {"Name": ['Ajay', 'Amit', 'Rohit', 'Himanshu', 'Ravi', 'Harsh'],
        "Age": [20,21,22,23,24,25],
        "Salary": [20000, 25000, 30000, 35000, 40000, 45000],
        "Performance Score": [90,89,88,87,86,85]}
df = pd.DataFrame(data)
print(df)
print("Modified Data")

df.drop(columns=['Performance Score','Age'], inplace = True)
print(df)