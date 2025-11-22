
import pandas as pd

data = {"Name": ['Ajay', 'Amit', 'Rohit', 'Himanshu', 'Ravi', 'Harsh'],
        "Age": [20,21,22,23,24,25],
        "Salary": [20000, 25000, 30000, 35000, 40000, 45000],
        "Performance Score": [90,89,88,87,86,85]}
df = pd.DataFrame(data)
print(df)

# .loc[]
# df.loc[row_index,'column_name'] = new_value

df.loc[0,'Salary'] = 120000
print(df)