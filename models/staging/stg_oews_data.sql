WITH source AS (
    SELECT * FROM {{ source('raw', 'raw_oews_data') }}
), 

renamed AS (
    SELECT 
        series_id, 
        CAST(year AS INT) AS year,
        period,
        CAST(value AS FLOAT) AS value,
        CAST(footnote_codes AS INT) AS footnote_codes
    FROM source
)

SELECT * FROM renamed