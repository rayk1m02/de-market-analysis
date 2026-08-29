WITH source AS (
    SELECT * FROM {{ source('raw', 'raw_laus_series') }}
),

renamed AS (
    SELECT 
        series_id,
        area,
        CASE
            WHEN area LIKE '%Austin%' THEN 'AUS'
            WHEN area LIKE '%Seattle%' THEN 'SEA'
            WHEN area LIKE '%Chicago%' THEN 'CHI'
            WHEN area LIKE '%Washington%' THEN 'DC'
            WHEN area LIKE '%New York%' THEN 'NY'
            ELSE 'UNK'
        END AS area_abbr,
        CASE
            WHEN RIGHT(series_id, 2) = '03' THEN 'unemployment_rate'
            WHEN RIGHT(series_id, 2) = '04' THEN 'unemployment'
            WHEN RIGHT(series_id, 2) = '05' THEN 'employment'
            WHEN RIGHT(series_id, 2) = '06' THEN 'labor_force'
        END AS measure_type
    FROM source
)

SELECT * FROM renamed