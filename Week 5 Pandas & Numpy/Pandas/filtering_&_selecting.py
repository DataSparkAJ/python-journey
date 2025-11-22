import pandas as pd

data = {"Name": ['Ajay', 'Amit', 'Rohit', 'Himanshu', 'Ravi', 'Harsh'],
        "Age": [20,21,22,23,24,25],
        "Salary": [20000, 25000, 30000, 35000, 40000, 45000],
        "Performance Score": [90,89,88,87,86,85]}
df = pd.DataFrame(data)
print("Sample Dataframe")
print(df)

# display the dataframe
print("Names (Single column return series)")
name = df['Name']
print(name)

# selecting multiple columns
subset = df[['Name', 'Salary']]
print("\nsubset with name and salary")
print(subset)

high_salary = df[df['Salary'] > 25000]
print("Employees with salary > 25000")
print(high_salary)

# filtering rows with multiple conditions
filtered = df[(df['Salary']>25000) & (df['Age'] > 23)]
print("Employee list age > 23 + salary > 25000")
print(filtered)

# using OR conditions
filtered_or = df[(df['Performance Score']> 86) | (df["Age"]> 20)]
print("Employees older than 20 or performance greater than 86")
print(filtered_or)