# pd.merge(df1,df2, on = 'Column name', how = 'type of join')

import pandas as pd

# customer dataframe
df_customer = pd.DataFrame({'Customer ID': [1,2,3],
                            "Name": ["Yash", "Gaurav", "Deepak"]})

# order dataframe
df_order = pd.DataFrame({'Customer ID': [1,2,4],
                         "Order": [4000,4500,3500]})

merged_df = pd.merge(df_customer,df_order, on = "Customer ID", how = 'inner')
print("Inner Join")
print(merged_df)