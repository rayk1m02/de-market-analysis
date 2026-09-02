# DE Market Analysis

Comparing Data Engineering adjacent labor market and Cost of Living data across AUS, SEA, CHI, DC, and NYC, using dbt and DuckDB.

## Data Sources

- **BLS LAUS** — monthly unemployment/labor force data per metro, via the BLS API
- **BLS OEWS** — employment and wages for DE-adjacent occupations per metro. Pulled from BLS's bulk flat files instead of the API, since the API only returned the recent year. Turns out, the flat files are also limited to recent year (2025), since BLS reissues new series IDs each release cycle rather than extending history. True multi-year depth will build up as this pipeline gets rerun over time. In hindsight, the API alone could have gotten a similar result with less file manipulation, but the flat files also provided essential area and occupation reference tables and were more reliable for pulling 340 specific series.
- **Census ACS** — COL data (income, rent, home value) per metro

## Notes
- All LAUS series use not-seasonally-adjusted data
- All LAUS series use Area type: Metropolitan areas
- Metropolitan areas selected:
    - Austin-Round Rock-San Marcos, TX
    - Seattle-Tacoma-Bellevue, WA
    - Chicago-Naperville-Elgin, IL-IN
    - Washington-Arlington-Alexandria, DC-VA-MD-WV
    - New York-Newark-Jersey City, NY-NJ
- COL data (ACS) lags roughly 1-2 years behind labor market data (LAUS/OEWS) due to each source's release cadence. Comparisons should be read as approximately concurrent, not simultaneous. 
- Worth noting that the OEWS data is a 2025 snapshot. Though this project will factor in the 2026 OEWS data once the figures come out, it currently reflects existing job statistics for that given date period and does not indicate to-date/future hiring trends and job volume. It also does not fully capture Data Engineering specifically, since no SOC code exists for the role. DBA and DB Architect remain the closest (imperfect) proxies.
- A small number of individual data points in the source LAUS data are suppressed by BLS (marked `-`) and converted to NULL in staging. This can surface as NaN in derived columns like month-over-month change.
- `labor_market_rank` in `fct_labor_market` will only compute when all five metros have data for a given month. BLS may publish the most recent month for some metros before others (Seattle's July 2026 data landed before Austin's), which would otherwise produce a misleading rank of 1 for a metro competing against no other.

## Insights
- DC's median household income exceeds NYC's ($126,684 vs. $99,155), likely reflecting DC's labor market concentration in high-paying government and consulting sectors, versus NYC's broader metro definition, which includes lower-cost outer boroughs / New Jersey suburbs.
- DC shows the highest Database Architect concentration of any metro (location quotient 3.5, rougly 3.5x the national average). This reinforces the previous finding on DC's labor market and its density in certain sectors and roles.
- Chicago has a larger raw Software Developer count than Austin (40,370 vs. 31,960), but a lower location quotient (0.82 vs. 2.28). As LQ measures *relative* concentration, this indicates software roles make up a larger share of Austin's overall economy than Chicago's.
- Across all five metros, Database Administrator and Database Architect roles consistently sit on the lower end of both employment and wages compared to Software Developer and Data Scientist, despite DBA being the closest occupational match to this project's own career target. Software Developer shows the highest wages and location quotients in nearly every metro, but it is also the broadest of the four occupations listed and is likely the most exposed to AI driven hiring shifts through 2026 and onwards.
- Database Architect's annual mean wage is higher than Software Developer's in 3 of 5 metros (Austin, Chicago, DC), while the reverse holds in Seattle and New York. Software Developer location quotient doesn't explain the split (Seattle and Austin both show high tech concentration, yet only one shows this pattern). The actual driver isn't clear from this data alone and would need further investigation.

## Setup

​```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
​```

​Create a `.env` file:

```BLS_API_KEY=your_key_here```

```ACS_API_KEY=your_key_here```