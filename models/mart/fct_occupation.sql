SELECT
    d.area_abbr,
    d.area_name,
    o.occupation_name,
    o.year,
    o.employment,
    o.hourly_mean_wage,
    o.annual_mean_wage,
    o.annual_median_wage,
    o.location_quotient
FROM {{ ref('int_oews_wide') }} o
LEFT JOIN {{ ref('dim_metro') }} d
    ON o.area_abbr = d.area_abbr