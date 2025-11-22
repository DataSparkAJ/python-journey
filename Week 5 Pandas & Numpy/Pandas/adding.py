import pandas as pd

data = {"Name": ['Ajay', 'Amit', 'Rohit', 'Himanshu', 'Ravi', 'Harsh'],
        "Age": [20,21,22,23,24,25],
        "Salary": [20000, 25000, 30000, 35000, 40000, 45000],
        "Performance Score": [90,89,88,87,86,85]}
df = pd.DataFrame(data)


df["Bonus"] = df['Salary'] * 0.1
print(df)

# using insert method
# df.insert(loc,"column name", data)

df.insert(0, "Employee ID", [10,20,30,40,50,60])
print(df)
