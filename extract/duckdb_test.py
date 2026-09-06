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

con.execute("""
    SELECT area_abbr, occupation_name, employment, annual_mean_wage, annual_median_wage, location_quotient, occupation_wage_rank, metro_wage_rank
    FROM fct_occupation
    ORDER BY area_abbr, occupation_wage_rank
    """).df()
con.execute("SELECT area_abbr, income, rent, home_value, metro_code, rent_rank_asc FROM fct_cost_of_living").df()

con.execute("""
    SELECT area_abbr, occupation_name, annual_mean_wage, rent, home_value, rent_pct_of_wage, years_to_afford_home 
    FROM mart_wage_vs_col 
    ORDER BY area_abbr, rent_pct_of_wage ASC
    """).df()

'''
other
- annual mean wage vs location quotient (does higher wage track with higher ocupational density)
    fct_occupation X fct_occupation
- correlation between annual mean wage and employment, factoring in location quotient
    fct_occupation X fct_occcupation
    does a higher employment count relate to wage level, and does concentration change that relationship?
- employment percentage per occupation, per metro 
    fct_occupation X fct_labor_market
    note - grain mismatch (monthly vs. annual snapshot) needs a decision on which labor_force month to use before building this
- labor force count / home value or rent value (does higher labor force count equate to higher or lower rent or home value / any correlation?) 
    - fct_labor_market X fct_acs_data
'''