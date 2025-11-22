'''
df['Column Name].mean()
df['Column Name].max()
df['Column Name].min()
df['Column Name].sum()
'''
import pandas as pd

data = {'Name': ['Arun','Kartik','Priyank'],
        'Salary': [10000,15000,20000],
        'Age': [35,29,24]}

df = pd.DataFrame(data)
avg_salary = df['Salary'].mean()
print(avg_salary)

