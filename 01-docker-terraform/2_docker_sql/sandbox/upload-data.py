#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from sqlalchemy import create_engine

pd.__version__

df = pd.read_parquet("yellow_tripdata_2023-01.parquet", "fastparquet")

pd.to_datetime(df.tpep_pickup_datetime)

pd.to_datetime(df.tpep_dropoff_datetime)


engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

engine.connect()

print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine))

df.head(n=0).to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')

df.to_sql(name='yellow_taxi_data', con=engine, if_exists='append')

