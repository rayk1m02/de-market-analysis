#%%
import duckdb
import os
print(os.getcwd())
# con = duckdb.connect("dev.duckdb")
con = duckdb.connect(r"C:\Users\rkim\Desktop\Learning\de-market-analysis\dev.duckdb")

# print(con.execute("SHOW TABLES").df())
#print(con.execute("SELECT table_schema, table_name FROM information_schema.tables").df())
# print(con.execute("SELECT * FROM raw_oews_series").df())
# print("")
# print(con.execute("SELECT * FROM raw_acs_data").df())
# print("")
# print(con.execute("SELECT * FROM raw_acs_data").df().dtypes)
# print("")
# print(con.execute("SELECT * FROM raw_oews_data").df().dtypes)
# print("")
# print(con.execute("SELECT * FROM stg_laus_data ORDER BY data_date LIMIT 10").df())
# print(con.execute("SELECT * FROM stg_laus_series").df())
# print(con.execute("SELECT * FROM stg_oews_data ORDER BY year LIMIT 20").df())
# print(con.execute("SELECT * FROM raw_oews_data").df())
print(con.execute("SELECT * FROM stg_acs_data ORDER BY income").df())
# %%