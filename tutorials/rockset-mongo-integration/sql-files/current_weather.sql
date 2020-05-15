select w.observation_time.value, w.temp
from commons.weather_data_collection as w
where w.observation_time.value is not NULL
order by w.observation_time.value DESC
limit 1;
