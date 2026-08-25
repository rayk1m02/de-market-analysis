# DE Market Analysis

Comparing DE-adjacent labor market and COL data across AUS, CHI, DC, and NYC, using dbt and DuckDB.

## Data Sources

- **BLS LAUS** — monthly unemployment/labor force data per metro, via the BLS API
- **BLS OEWS** — employment and wages for DE-adjacent occupations per metro. The API only returns the current year, so historical data comes from BLS's bulk flat files instead.
- **Census ACS** — cost-of-living data (income, rent, home value) per metro

## Setup

​```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
​```

Create a `.env` file:
​```
BLS_API_KEY=your_key_here
​```