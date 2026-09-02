SELECT
    d.area_abbr,
    d.area_name,
    l.data_date,
    l.unemployment_rate,
    l.unemployment,
    l.employment,
    l.labor_force,
    'Compute Metrics of Interest and Value'
FROM {{ ref('int_laus_wide') }} l
LEFT JOIN {{ ref('dim_metro') }} d
    ON l.area_abbr = d.area_abbr