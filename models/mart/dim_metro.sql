# descriptive information about the five metros

WITH laus_metros AS (
    SELECT DISTINCT
        area_abbr,
        area AS area_name
    FROM {{ ref('stg_laus_series') }}
),

oews_metros AS (
    SELECT DISTINCT
        area_abbr,
        area_code AS oews_area_code
    FROM {{ ref('stg_oews_series') }}
), 

acs_metros AS (
    SELECT DISTINCT
        area_abbr,
        metro_code AS acs_cbsa_code
    FROM {{ ref('stg_acs_data') }}
)

SELECT 
    l.area_abbr,
    l.area_name,
    o.oews_area_code,
    a.acs_cbsa_code
FROM laus_metros l
LEFT JOIN oews_metros o
    ON l.area_abbr = o.area_abbr
LEFT JOIN acs_metros a
    ON l.area_abbr = a.area_abbr