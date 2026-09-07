"""
Exports our final mart and fact models to CSVs (with readability in mind) 
for quick review and without needing to run the full pipeline. 
Formatting is applied here only and for display purposes. 
The underlying dbt modesl keep raw, unformatted numeric types.
"""
import duckdb
import pandas as pd
import os

con = duckdb.connect("dev.duckdb")

def fmt_currency(x):
    return "" if pd.isna(x) else f"${x:,.0f}"

def fmt_number(x):
    return "" if pd.isna(x) else f"{x:,.0f}"

def fmt_pct(x):
    return "" if pd.isna(x) else f"{x:.2f}%"

def fmt_decimal(x, decimals=2):
    return "" if pd.isna(x) else f"{x:.{decimals}f}"

os.makedirs("output", exist_ok=True) # if directory DNE, create it, else nothing

# fct_occupation
df = con.execute("""
    SELECT 
        area_abbr, 
        occupation_name, 
        employment, 
        hourly_mean_wage,
        annual_mean_wage, 
        annual_median_wage, 
        location_quotient,
        occupation_wage_rank, 
        metro_wage_rank, 
        mean_median_wage_gap
    FROM fct_occupation
    ORDER BY area_abbr, occupation_wage_rank
""").df()
df["employment"] = df["employment"].apply(fmt_number)
df["hourly_mean_wage"] = df["hourly_mean_wage"].apply(fmt_currency)
df["annual_mean_wage"] = df["annual_mean_wage"].apply(fmt_currency)
df["annual_median_wage"] = df["annual_median_wage"].apply(fmt_currency)
df["location_quotient"] = df["location_quotient"].apply(fmt_decimal)
df["mean_median_wage_gap"] = df["mean_median_wage_gap"].apply(fmt_currency)
df.to_csv("output/fct_occupation.csv", index=False)

# mart_wage_vs_col
df = con.execute("""
    SELECT 
        area_abbr, 
        occupation_name, 
        annual_mean_wage, 
        rent,
        home_value, 
        rent_pct_of_wage, 
        years_to_afford_home
    FROM mart_wage_vs_col
    ORDER BY area_abbr, rent_pct_of_wage
""").df()
df["annual_mean_wage"] = df["annual_mean_wage"].apply(fmt_currency)
df["rent"] = df["rent"].apply(fmt_currency)
df["home_value"] = df["home_value"].apply(fmt_currency)
df["rent_pct_of_wage"] = df["rent_pct_of_wage"].apply(fmt_pct)
df["years_to_afford_home"] = df["years_to_afford_home"].apply(fmt_decimal)
df.to_csv("output/mart_wage_vs_col.csv", index=False)

# mart_occupation_share
df = con.execute("""
    SELECT 
        area_abbr, 
        occupation_name, 
        employment, 
        avg_labor_force_2025,
        occupation_share_pct
    FROM mart_occupation_share
    ORDER BY area_abbr, occupation_name
""").df()
df["employment"] = df["employment"].apply(fmt_number)
df["avg_labor_force_2025"] = df["avg_labor_force_2025"].apply(fmt_number)
df["occupation_share_pct"] = df["occupation_share_pct"].apply(fmt_pct)
df.to_csv("output/mart_occupation_share.csv", index=False)

# mart_labor_force_vs_col
df = con.execute("""
    SELECT
        area_abbr,
        avg_labor_force_2025,
        rent,
        home_value
    FROM mart_labor_force_vs_col
""").df()
df["avg_labor_force_2025"] = df["avg_labor_force_2025"].apply(fmt_number)
df["rent"] = df["rent"].apply(fmt_currency)
df["home_value"] = df["home_value"].apply(fmt_currency)
df.to_csv("output/mart_labor_force_vs_col.csv", index=False)

print("Exported 4 CSVs to output/")
con.close()