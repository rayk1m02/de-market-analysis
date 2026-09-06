WITH labor_force_2025_avg AS (
    SELECT
        area_abbr,
        AVG(labor_force) AS avg_labor_force_2025
    FROM {{ ref('fct_labor_market') }}
    WHERE EXTRACT(YEAR FROM data_date) = 2025
    GROUP BY area_abbr
)

SELECT
    d.area_abbr,
    d.area_name,
    l.avg_labor_force_2025,
    c.rent,
    c.home_value
FROM labor_force_2025_avg l
LEFT JOIN {{ ref('fct_cost_of_living') }} c
    ON l.area_abbr = c.area_abbr
LEFT JOIN {{ ref('dim_metro') }} d
    ON l.area_abbr = d.area_abbr    