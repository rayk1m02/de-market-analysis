SELECT
    d.area_abbr,
    d.area_name,
    o.occupation_name,
    o.year,
    o.employment,
    o.hourly_mean_wage,
    o.annual_mean_wage,
    o.annual_median_wage,
    o.location_quotient,
    RANK() OVER (PARTITION BY o.area_abbr ORDER BY o.annual_mean_wage DESC) AS occupation_wage_rank,
    ROUND(o.annual_mean_wage - o.annual_median_wage, 2) AS mean_median_wage_gap
FROM {{ ref('int_oews_wide') }} o
LEFT JOIN {{ ref('dim_metro') }} d
    ON o.area_abbr = d.area_abbr