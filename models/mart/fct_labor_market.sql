SELECT
    d.area_abbr,
    d.area_name,
    l.data_date,
    l.unemployment_rate,
    l.unemployment,
    l.employment,
    l.labor_force,
    ROUND((
        l.employment - (LAG(l.employment) OVER (PARTITION BY l.area_abbr ORDER by l.data_date))) / 
        (LAG(l.employment) OVER (PARTITION BY l.area_abbr ORDER BY l.data_date)
    ) * 100, 2) AS emp_pct_change
FROM {{ ref('int_laus_wide') }} l
LEFT JOIN {{ ref('dim_metro') }} d
    ON l.area_abbr = d.area_abbr