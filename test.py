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
# oe.area
area_codes = ["0012420", "0042660", "0016980", "0047900", "0035620"]  # AUS, SEA, CHI, DC, NYC
# oe.occupation
occupation_codes = ["151242", "151243", "152051", "151252"]  # DB Admin, DB Architect, Data Scientist, Software Dev

area_str = ", ".join(f"'{a}'" for a in area_codes)
occ_str = ", ".join(f"'{o}'" for o in occupation_codes)

area_str
occ_str
# %%
