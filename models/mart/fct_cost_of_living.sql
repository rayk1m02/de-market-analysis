SELECT
    d.area_abbr,
    d.area_name,
    a.income,
    a.rent,
    a.home_value,
    a.metro_code,
    RANK() OVER (ORDER BY rent DESC) AS rent_rank_asc
FROM {{ ref('stg_acs_data') }} a
LEFT JOIN {{ ref('dim_metro') }} d
    ON a.area_abbr = d.area_abbr