import duckdb
con = duckdb.connect("dev.duckdb")
con.execute("DROP TABLE raw_acs_series")
print(con.execute("SHOW TABLES").df())
print(con.execute("SELECT table_schema, table_name FROM information_schema.tables").df())