#%%
from dotenv import load_dotenv
import os
import duckdb

load_dotenv()
api_key = os.getenv("BLS_API_KEY")
print(api_key)

con = duckdb.connect("dev.duckdb")
con.execute("SELECT * FROM raw_laus_data").df()
# %%