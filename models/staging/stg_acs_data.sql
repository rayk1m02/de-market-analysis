WITH SOURCE AS (
    SELECT * FROM {{ source('raw', 'raw_acs_data') }}
),

renamed AS (
    SELECT 
        NAME AS area,
        CASE
            WHEN NAME LIKE '%Austin%' THEN 'AUS'
            WHEN NAME LIKE '%Seattle%' THEN 'SEA'
            WHEN NAME LIKE '%Chicago%' THEN 'CHI'
            WHEN NAME LIKE '%Washington%' THEN 'DC'
            WHEN NAME LIKE '%New York%' THEN 'NY'
            ELSE 'UNK'
        END AS area_abbr,
        CAST(B19013_001E AS FLOAT) AS income,
        CAST(B25031_001E AS FLOAT) AS rent,
        CAST(B25077_001E AS FLOAT) AS home_value,
        "metropolitan statistical area/micropolitan statistical area" AS metro_code
    FROM SOURCE
)

SELECT * FROM renamed