SELECT
    s.area_abbr AS area_abbr,
    d.data_date AS data_date,
    CASE
        WHEN s.measure_type = 'unemployment_rate'
            THEN d.value 
        ELSE NULL
    END AS unemployment_rate,
    CASE
        WHEN s.measure_type = 'unemployment'
            THEN d.value 
        ELSE NULL
    END AS unemployment,
    CASE
        WHEN s.measure_type = 'employment'
            THEN d.value 
        ELSE NULL
    END AS employment,
    CASE
        WHEN s.measure_type = 'labor_force'
            THEN d.value 
        ELSE NULL
    END AS labor_force
FROM {{ ref('stg_laus_series') }} s
LEFT JOIN {{ ref('stg_laus_data') }} d
ON d.series_id = s.series_id