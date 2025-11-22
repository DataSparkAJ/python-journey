import pandas as pd


data = {"Name": ['Ajay', 'Ram', 'Shyam', 'Tony'],
                  "Age": [20,25,30,35],
                  "City": ['Kashipur','Nagpur','Madras', 'Madurai']}
df = pd.DataFrame(data)
print(df)

# df.to_csv("output.csv", index = False)
# df.to_excel("output.xlsx", index = False)
df.to_json("output.json", index = False)