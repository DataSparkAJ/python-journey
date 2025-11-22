import pandas as pd

data = {
  'Time': [1,2,3,4],
  'Value': [10,None,30,None]
}
df = pd.DataFrame(data)
print("Before Interpolation")
print(df)

df['Value'] = df['Value'].interpolate(method='linear')
print("After Interpolation")
print(df)

'''
1- time series data
2- numeric data with trend
3- avoid dropping rows
'''