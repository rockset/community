SELECT
    COUNT(i.orderid) AS orders,
    SUM(i.orderunits) AS units,
    i.address.zipcode,
    i.address.state,
    -- bucket data in one hour buckets
    TIME_BUCKET(HOURS(1), TIMESTAMP_MILLIS(i.ordertime)) AS _event_time
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
