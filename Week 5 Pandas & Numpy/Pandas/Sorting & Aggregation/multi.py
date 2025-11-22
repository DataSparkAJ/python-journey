import pandas as pd

data = {'Name': ['Arun','Kartik','Priyank','Anmol','Vipin','Sumit'],
        'Salary': [10000,15000,20000,32000,12000,18000],
        'Age': [35,29,24,23,22,24]}

df = pd.DataFrame(data)
grouped = df.groupby(['Age','Name'])['Salary'].sum()
print(grouped)