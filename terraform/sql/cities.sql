SELECT
    c.fields.country,
    count(c.fields.name) as cities
FROM
    community.cities as c
GROUP BY
    country
ORDER by
    cities DESC
