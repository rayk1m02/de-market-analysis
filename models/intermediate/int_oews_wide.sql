SELECT
    s.area_abbr AS area_abbr,
    s.occupation_name as occupation_name,
    d.year AS year,
    MAX(CASE WHEN s.measure_type = 'employment' THEN d.value END) AS employment,
    MAX(CASE WHEN s.measure_type = 'hourly_mean_wage' THEN d.value END) AS hourly_mean_wage,
    MAX(CASE WHEN s.measure_type = 'annual_mean_wage' THEN d.value END) AS annual_mean_wage,
    MAX(CASE WHEN s.measure_type = 'annual_median_wage' THEN d.value END) AS annual_median_wage,
    MAX(CASE WHEN s.measure_type = 'location_quotient' THEN d.value END) AS location_quotient
FROM {{ ref('stg_oews_data') }} d
LEFT JOIN {{ ref('stg_oews_series') }} s
    ON d.series_id = s.series_id
WHERE s.measure_type IN ('employment', 'hourly_mean_wage', 'annual_mean_wage', 'annual_median_wage', 'location_quotient')
GROUP BY s.area_abbr, s.occupation_name, d.year