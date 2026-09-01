SELECT
    s.area_abbr AS area_abbr,
    d.data_date AS data_date,
    MAX(CASE WHEN s.measure_type = 'unemployment_rate' THEN d.value END) AS unemployment_rate,
    MAX(CASE WHEN s.measure_type = 'unemployment' THEN d.value END) AS unemployment,    
    MAX(CASE WHEN s.measure_type = 'employment' THEN d.value END) AS employment,
    MAX(CASE WHEN s.measure_type = 'labor_force' THEN d.value END) AS labor_force
FROM {{ ref('stg_laus_data') }} d
LEFT JOIN {{ ref('stg_laus_series') }} s
    ON d.series_id = s.series_id
GROUP BY s.area_abbr, d.data_date