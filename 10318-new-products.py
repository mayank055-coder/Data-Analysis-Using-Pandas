https://platform.stratascratch.com/coding/10318-new-products?code_type=2
# Import your libraries
import pandas as pd

# Start writing code
car_launches.head()

df=pd.pivot_table(car_launches,index = 'company_name',columns ='year',values = 'product_name', aggfunc = 'count').reset_index()
df['diff'] = df[2020] - df[2019]
df[['company_name','diff']]
