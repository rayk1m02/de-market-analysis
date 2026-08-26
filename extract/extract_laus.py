import requests
import pandas as pd
import duckdb
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("BLS_API_KEY")

# Each metro maps to 4 series IDs, stored long (one row per series): unemployment rate, unemployment, employment, labor force.
series_ids = {
    "austin": ["LAUMT481242000000003", "LAUMT481242000000004", "LAUMT481242000000005", "LAUMT481242000000006"],
    "seattle": ["LAUMT534266000000003", "LAUMT534266000000004", "LAUMT534266000000005", "LAUMT534266000000006"],
    "chicago": ["LAUMT171698000000003", "LAUMT171698000000004", "LAUMT171698000000005", "LAUMT171698000000006"],
    "dc": ["LAUMT114790000000003", "LAUMT114790000000004", "LAUMT114790000000005", "LAUMT114790000000006"],
    "nyc": ["LAUMT363562000000003", "LAUMT363562000000004", "LAUMT363562000000005", "LAUMT363562000000006"]
}

def extract_laus(series_ids, start_year="2016", end_year="2026"):
    url = "https://api.bls.gov/publicAPI/v2/timeseries/data/"

    # all_series = []
    # for metro_series in series_ids.values():
    #     for sid in metro_series:
    #         all_series.append(sid)

    # nested list comprehension
    all_series = [sid for metro_series in series_ids.values() for sid in metro_series]

    payload = {
        "seriesid": all_series,
        "startyear": start_year,
        "endyear": end_year,
        "catalog": True,
        "calculations": True,
        "annualaverage": True,
        "aspects": False,
        "registrationkey": api_key
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()
    data = response.json()

    series_lookup = [] # catalog data for metadata (area name, occupation, etc)
    records = [] # raw data table
    for series in data["Results"]["series"]:
        series_lookup.append({
            "series_id": series["seriesID"],
            "area": series["catalog"]["area"],
            "series_title": series["catalog"]["series_title"]
            # add more fields later if needed
        })
        for point in series["data"]:
            records.append({
                "series_id": series["seriesID"],
                "year": point["year"],
                "period": point["period"],
                "period_name": point["periodName"],
                "value": point["value"],
            })

    df_lookup = pd.DataFrame(series_lookup).drop_duplicates()
    df_data = pd.DataFrame(records)
    
    return df_lookup, df_data

if __name__ == "__main__":
    df_lookup, df_data = extract_laus(series_ids)
    con = duckdb.connect("dev.duckdb")
    con.execute("CREATE OR REPLACE TABLE raw_laus_series AS SELECT * FROM df_lookup")
    con.execute("CREATE OR REPLACE TABLE raw_laus_data AS SELECT * FROM df_data")
    print(f"Loaded {len(df_lookup)} series, {len(df_data)} data rows")