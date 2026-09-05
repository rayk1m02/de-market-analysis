#%%
import duckdb
import os
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_rows', None)
# con = duckdb.connect("dev.duckdb")
con = duckdb.connect(r"C:\Users\rkim\Desktop\Learning\de-market-analysis\dev.duckdb")

con.execute("SELECT * FROM stg_laus_series").df() 
con.execute("SELECT * FROM stg_laus_data").df()
con.execute("SELECT * FROM stg_oews_series LIMIT 5").df()
con.execute("SELECT * FROM stg_oews_data LIMIT 5").df()
con.execute("SELECT * FROM stg_acs_data").df()

con.execute("SELECT * FROM int_laus_wide ORDER BY area_abbr, data_date DESC LIMIT 10").df()
con.execute("SELECT * FROM int_oews_wide ORDER BY area_abbr, occupation_name LIMIT 25").df()

con.execute("SELECT * FROM dim_metro").df()
con.execute("SELECT * FROM fct_labor_market ORDER BY area_abbr DESC, data_date DESC LIMIT 10").df()
con.execute("SELECT * FROM fct_occupation ORDER BY area_abbr DESC").df()