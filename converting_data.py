#converting .parquet into .csv to be imported inside microstrategy BI tool
#this step is done to perform more interactive analysis
#the wd is where I have downloaded the .parquet files

import pandas as pd

df = pd.read_parquet('orders_data.parquet')
df.to_csv('orders_data.csv')

df = pd.read_parquet('products_data.parquet')
df.to_csv('products_data.csv')