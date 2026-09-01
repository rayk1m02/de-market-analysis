WITH source AS (
    SELECT * FROM {{ source('raw', 'raw_oews_series') }}
), 

renamed AS (
    SELECT 
        series_id,
        seasonal,
        areatype_code,
        industry_code,
        occupation_code,
        datatype_code,
        CAST(state_code AS INT) AS state_code,
        area_code,
        sector_code,
        series_title,
        CAST(footnote_codes AS INT) AS footnote_codes,
        CAST(begin_year AS INT) AS begin_year,
        begin_period,
        CAST(end_year AS INT) AS end_year,
        end_period,
        CASE
            WHEN occupation_code = '151242' THEN 'Database Administrators'
            WHEN occupation_code = '151243' THEN 'Database Architects'
            WHEN occupation_code = '152051' THEN 'Data Scientists'
            WHEN occupation_code = '151252' THEN 'Software Developers'
        END AS occupation_name,
        CASE
            WHEN datatype_code = '01' THEN 'employment'
            WHEN datatype_code = '03' THEN 'hourly_mean_wage'
            WHEN datatype_code = '04' THEN 'annual_mean_wage'
            WHEN datatype_code = '13' THEN 'annual_median_wage'
            WHEN datatype_code = '17' THEN 'location_quotient'
            ELSE 'other'
        END AS measure_type,
        CASE
            WHEN area_code = '0012420' THEN 'AUS'
            WHEN area_code = '0042660' THEN 'SEA'
            WHEN area_code = '0016980' THEN 'CHI'
            WHEN area_code = '0047900' THEN 'DC'
            WHEN area_code = '0035620' THEN 'NY'
        END AS area_abbr
    FROM source
)

SELECT * FROM renamed