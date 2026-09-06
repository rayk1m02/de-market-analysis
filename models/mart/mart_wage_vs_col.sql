SELECT
    d.area_abbr,
    d.area_name,
    o.occupation_name,
    o.annual_mean_wage,
    c.rent,
    c.home_value,
    ROUND((c.rent * 12) / o.annual_mean_wage * 100, 2) AS rent_pct_of_wage,
    ROUND(c.home_value / o.annual_mean_wage, 2) AS years_to_afford_home
FROM {{ ref('fct_occupation') }} o
LEFT JOIN {{ ref('fct_cost_of_living') }} c
    ON o.area_abbr = c.area_abbr
LEFT JOIN {{ ref('dim_metro') }} d
    ON o.area_abbr = d.area_abbr