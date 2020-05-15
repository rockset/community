WITH pm10avg AS (
select AVG(a.pm10.value) avg_pm10, EXTRACT(date from PARSE_TIMESTAMP_ISO8601(a.observation_time.value)) date_pm10
from commons.air_pollution_data_collection a
GROUP BY date_pm10
),
 tempavg as (
SELECT AVG(w.temp.value) avg_weather, EXTRACT(date from PARSE_TIMESTAMP_ISO8601(w.observation_time.value)) date_weather
from commons.weather_data_collection w
 GROUP BY date_weather, aq_date
 ) select pm10avg.avg_pm10, tempavg.avg_weather, pm10avg.date_pm10
 from pm10avg
 join tempavg on pm10avg.date_pm10 = tempavg.date_weather
 ORDER BY date_pm10 DESC;
