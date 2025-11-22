import pandas as pd


df = pd.read_json("sample_Data.json")
print(df)

print("First 5 rows of the table")
print(df.head())

print("Last 5 rows of the table")
print(df.tail())