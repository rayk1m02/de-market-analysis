# DE Market Analysis

Comparing DE-adjacent labor market and COL data across AUS, SEA, CHI, DC, and NYC, using dbt and DuckDB.

## Data Sources

- **BLS LAUS** — monthly unemployment/labor force data per metro, via the BLS API
- **BLS OEWS** — employment and wages for DE-adjacent occupations per metro. The API only returns the current year, so historical data comes from BLS's bulk flat files instead.
- **Census ACS** — cost-of-living data (income, rent, home value) per metro

## Notes
- All LAUS series use not-seasonally-adjusted data
- All LAUS series use Area type: Metropolitan areas
- Metropolitan areas selected:
    - Austin-Round Rock-San Marcos, TX
    - Seattle-Tacoma-Bellevue, WA
    - Chicago-Naperville-Elgin, IL-IN
    - Washington-Arlington-Alexandria, DC-VA-MD-WV
    - New York-Newark-Jersey City, NY-NJ

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