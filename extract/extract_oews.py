'''
https://download.bls.gov/pub/time.series/oe/

oe.area
    48	0012420	M	Austin-Round Rock-San Marcos, TX
    53	0042660	M	Seattle-Tacoma-Bellevue, WA
    17	0016980	M	Chicago-Naperville-Elgin, IL-IN
    11	0047900	M	Washington-Arlington-Alexandria, DC-VA-MD-WV
    36	0035620	M	New York-Newark-Jersey City, NY-NJ

oe.occupation
    151242	Database Administrators
    151243	Database Architects
    152051	Data Scientists
    151252	Software Developers

oe.series (raw_downloads dir, column headers below)
    series_id seasonal areatype_code industry_code occupation_code datatype_code state_code area_code sector_code series_title footnote_codes begin_year begin_period end_year end_period

oe.alldata (raw_downloads dir, column headers below)
    series_id year period value footnote_codes
'''
import duckdb
import pandas as pd

con = duckdb.connect("dev.duckdb")

# oe.area
area_codes = ["0012420", "0042660", "0016980", "0047900", "0035620"]  # AUS, SEA, CHI, DC, NYC
# oe.occupation
occupation_codes = ["151242", "151243", "152051", "151252"]  # DB Admin, DB Architect, Data Scientist, Software Dev

# SQL requires literal, comma-separated list of quoted values
area_str = ", ".join(f"'{a}'" for a in area_codes) # "'0012420', '0042660', '0016980', '0047900', '0035620'"
occ_str = ", ".join(f"'{o}'" for o in occupation_codes) # "'151242', '151243', '152051', '151252'"

# Filter oe.series down to just target metros and occupations across all industries
# areatype_code 'M' guarantees metro filter
# industry_code '000000' is code for cross-industry/all-industries combined
con.execute(f"""
    CREATE OR REPLACE TABLE raw_oews_series AS
    SELECT * FROM read_csv('extract/raw_downloads/oe_series', delim='\t', header=true)
    WHERE trim(area_code) IN ({area_str})
        AND trim(occupation_code) IN ({occ_str})
        AND trim(areatype_code) = 'M' 
        AND trim(industry_code) = '000000'
""")

# convert to DataFrame, pull just the series_id column as a Series, and convert into a list for Python to use for SQL
target_ids = con.execute("SELECT trim(series_id) AS series_id FROM raw_oews_series").df()["series_id"].tolist() 
ids_str = ", ".join(f"'{sid}'" for sid in target_ids)

# Filter oe.alldata
con.execute(f"""
    CREATE OR REPLACE TABLE raw_oews_data AS
    SELECT * FROM read_csv('extract/raw_downloads/oe_alldata', delim='\t', header=true)
    WHERE trim(series_id) IN ({ids_str})
""")

if __name__ == "__main__":
    print(con.execute("SELECT COUNT(*) FROM raw_oews_series").df())
    # oews.alldata is categorized by datatype_code suffix. We will use our staging models to make sense between oews.series and oews.data
    print(con.execute("SELECT COUNT(*) FROM raw_oews_data").df())