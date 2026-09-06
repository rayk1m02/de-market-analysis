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

con.execute("SELECT CORR(annual_mean_wage, location_quotient) FROM fct_occupation").df()
con.execute("SELECT CORR(annual_mean_wage, employment) FROM fct_occupation").df()

con.execute("SELECT area_abbr, occupation_name, employment, avg_labor_force_2025, occupation_share_pct FROM mart_occupation_share").df()
con.execute("SELECT * FROM mart_labor_force_vs_col").df()
con.execute("""
    SELECT 
        CORR(avg_labor_force_2025, rent) AS corr_labor_force_rent,
        CORR(avg_labor_force_2025, home_value) AS corr_labor_force_home_value
    FROM mart_labor_force_vs_col
""").df()