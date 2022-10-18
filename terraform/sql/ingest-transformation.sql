SELECT
    COUNT(i.orderid) AS orders,
    SUM(i.orderunits) AS units,
    i.address.zipcode,
    i.address.state,
    -- bucket data in five minute buckets
    TIME_BUCKET(MINUTES(5), TIMESTAMP_MILLIS(i.ordertime)) AS _event_time
FROM
    _input AS i
WHERE
    -- drop all records with an incorrect state
	i.address.state != 'State_'
GROUP BY
	_event_time,
    i.address.zipcode,
    i.address.state
-- CLUSTER BY
-- 	state
