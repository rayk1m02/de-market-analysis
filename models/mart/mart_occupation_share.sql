WITH labor_force_2025_avg AS (
    SELECT
        area_abbr,
        AVG(labor_force) AS avg_labor_force_2025
    FROM {{ ref('fct_labor_market') }}
    WHERE EXTRACT(YEAR FROM data_date) = 2025
    GROUP BY area_abbr
)

SELECT
    o.area_abbr,
    d.area_name,
    o.occupation_name,
    o.employment,
    l.avg_labor_force_2025,
    ROUND(o.employment / l.avg_labor_force_2025 * 100, 4) AS occupation_share_pct
FROM {{ ref('fct_occupation') }} o
LEFT JOIN labor_force_2025_avg l
    ON o.area_abbr = l.area_abbr
LEFT JOIN {{ ref('dim_metro') }} d
    ON o.area_abbr = d.area_abbr