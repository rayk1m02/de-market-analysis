WITH source AS (
    SELECT * FROM {{ source('raw', 'raw_laus_data') }}
),

renamed AS (
    SELECT 
        series_id,
        CAST(year || '-' || SUBSTRING(period, 2, 2) || '-01' AS DATE) AS data_date,
        period,
        period_name, 
        CASE 
            WHEN value = '-' THEN NULL
            ELSE CAST(value AS FLOAT)
        END AS value
    FROM source
    WHERE period != 'M13'
)

SELECT * FROM renamed