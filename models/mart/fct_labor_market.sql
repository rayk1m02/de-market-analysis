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
    ) * 100, 2) AS emp_pct_change,
    ROUND((l.unemployment_rate - (LAG(l.unemployment_rate) OVER (PARTITION By l.area_abbr ORDER BY l.data_date))), 2) AS unemp_rate_pp_change,
    ROUND(AVG(l.unemployment_rate) OVER (
        PARTITION BY l.area_abbr
        ORDER BY l.data_date
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ), 2) AS unemp_rate_3mo_avg,
    CASE
        WHEN COUNT(*) OVER (PARTITION BY l.data_date) = 5 THEN 
            RANK() OVER (PARTITION BY l.data_date ORDER BY l.unemployment_rate ASC) 
        ELSE NULL
    END AS labor_market_rank
FROM {{ ref('int_laus_wide') }} l
LEFT JOIN {{ ref('dim_metro') }} d
    ON l.area_abbr = d.area_abbr