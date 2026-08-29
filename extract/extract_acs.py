'''
https://api.census.gov/data/2024/acs/acs5

ACS 5-Year Estimates (used instead of 1-year, for consistent coverage across all 5 metros regardless of population size)

Geography — CBSA (Core-Based Statistical Area) codes. Identical to BLS OEWS area codes but with no leading zeros
    12420   Austin-Round Rock-San Marcos, TX
    42660   Seattle-Tacoma-Bellevue, WA
    16980   Chicago-Naperville-Elgin, IL-IN
    47900   Washington-Arlington-Alexandria, DC-VA-MD-WV
    35620   New York-Newark-Jersey City, NY-NJ

Variables (get= parameter)
    NAME            human-readable area name (always available, no lookup needed)
    B19013_001E     median household income (past 12 months)
    B25031_001E     median gross rent, total across all bedroom counts
    B25077_001E     median home value

Query shape:
    ?get=NAME,B19013_001E,B25031_001E,B25077_001E
    &for=metropolitan statistical area/micropolitan statistical area:{cbsa_code}
    &key={api_key}

    https://api.census.gov/data/2024/acs/acs5
    ?get=NAME,B19013_001E,B25031_001E,B25077_001E
    &for=metropolitan%20statistical%20area/micropolitan%20statistical%20area:12420
    &key=ACS_KEY
'''
import requests
import pandas as pd
import duckdb
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("ACS_API_KEY")

geography_ids = {
    "austin": "12420",
    "seattle": "42660",
    "chicago": "16980",
    "dc": "47900",
    "nyc": "35620"
}

acs_value_ids = ["NAME", "B19013_001E", "B25031_001E", "B25077_001E"]

def extract_acs(geography_ids, acs_value_ids, api_key):
    url = "https://api.census.gov/data/2024/acs/acs5"

    record = []

    for metro, geo_id in geography_ids.items():
        get_str = ",".join(acs_value_ids) # "Name,B19013_001E,B25031_001E,B25077_001E"
        params = {
            "get": get_str,
            "for": "metropolitan statistical area/micropolitan statistical area:" + geo_id,
            "key": api_key
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        result = response.json() # response is in the format [["header1", "header2", ...], ["value1", "value2", ...]]
        row = dict(zip(result[0], result[1])) # zip() pairs each header with corresponding value into tuples, dict() turns into key-value pairs.
        record.append(row)

    data = pd.DataFrame(record)
    return data        

if __name__ == "__main__":
    df_data = extract_acs(geography_ids, acs_value_ids, api_key)
    con = duckdb.connect("dev.duckdb")
    con.execute("CREATE OR REPLACE TABLE raw_acs_series AS SELECT * from df_data")
    print(f"Loaded {len(df_data)} data rows")