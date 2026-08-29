#%%
import duckdb
con = duckdb.connect("dev.duckdb")
# print(con.execute("SHOW TABLES").df())
# print(con.execute("SELECT table_schema, table_name FROM information_schema.tables").df())
# print(con.execute("SELECT * FROM raw_laus_series").df())
# print(con.execute("SELECT * FROM raw_laus_data").df())
# print(con.execute("SELECT * FROM raw_laus_data").df().describe())
# print(con.execute("SELECT * FROM raw_laus_data").df().dtypes)
print(con.execute("SELECT * FROM stg_laus_data ORDER BY data_date LIMIT 10").df())
