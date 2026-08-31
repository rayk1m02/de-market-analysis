#%%
import duckdb
import os
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
# con = duckdb.connect("dev.duckdb")
con = duckdb.connect(r"C:\Users\rkim\Desktop\Learning\de-market-analysis\dev.duckdb")

con.execute("SELECT * FROM stg_laus_series").df() 
con.execute("SELECT * FROM stg_laus_data").df()
con.execute("SELECT * FROM stg_oews_series").df()
con.execute("SELECT * FROM stg_oews_data").df()
con.execute("SELECT * FROM stg_acs_data").df()