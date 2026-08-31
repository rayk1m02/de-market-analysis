SELECT
    s.area_abbr AS area_abbr,
    d.data_date AS data_date,
    '' AS unemployment_rate,
    '' AS unemployment,
    '' AS employment,
    '' AS labor_force
FROM {{ ref('stg_laus_series') }} s
LEFT JOIN {{ ref('stg_laus_data') }} d
ON d.series_id = s.series_id