from settings import *
from mongo_config import weather_data_collection, pollution_data_collection
from timeloop import Timeloop
from datetime import timedelta
import requests
import json
from rockset import Client, ParamDict

tl = Timeloop()

def get_weather_data():
    """ get weather data from climacell """
    url = "https://api.climacell.co/v3/weather/realtime"
    querystring = {"lat":"39.9042","lon":"116.4074","unit_system":"us","fields":"precipitation,wind_gust,humidity,wind_direction,precipitation_type,visibility,cloud_cover,cloud_base,cloud_ceiling,weather_code,feels_like,temp","apikey":CLIMACELL_API_KEY}
    weather_response = requests.request("GET", url, params=querystring)
    return weather_response.json()

def get_air_pollution_data():
    """ get air quality data from climacell """
    url = "https://api.climacell.co/v3/weather/realtime"
    querystring = {"lat":"39.9042","lon":"116.4074","unit_system":"us","fields":"o3,so2,co,no2,pm10,pm25","apikey":CLIMACELL_API_KEY}
    air_pollution_response = requests.request("GET", url, params=querystring)
    return air_pollution_response.json()

@tl.job(interval=timedelta(seconds=120))
def sample_job_every_120s():
    weather_response = get_weather_data()
    air_pollution_data = get_air_pollution_data()
    insert_to_mongo(weather_response, air_pollution_data)

def insert_to_mongo(weather_data, air_pollution_data):
    """ insert weather data and traffic data to the proper collections """
    weather_data_collection.insert_one(weather_data)
    pollution_data_collection.insert_one(air_pollution_data)
    make_requests()

def make_requests():
    avg_pm10_data = get_avg_pm10_results()
    current_weather_results = get_current_weather_results()
    display_data(avg_pm10_data, current_weather_results)

def get_current_weather_results():
    r = requests.post('https://api.rs2.usw2.rockset.com/v1/orgs/self/ws/commons/lambdas/YOUR QUERY LAMBDA NAME /versions/YOUR-VERSION-NUMBER',
    headers={'Authorization': 'ApiKey '+ ROCKSET_API_KEY})
    return r.json()

def get_avg_pm10_results():
    rs = Client(api_key=ROCKSET_API_KEY, api_server='https://api.rs2.usw2.rockset.com')

    # retrieve Query Lambda
    qlambda = rs.QueryLambda.retrieve(
    'YOUR QUERY LAMBDA NAME',
    version=4,
    workspace='commons'
        )
    params = ParamDict()
    results = qlambda.execute(parameters=params)
    return results.results

def display_data(avg_pm10_data, weather_results):
    print("****************************************************\n")
    pm10_data = (avg_pm10_data[0]['avg_pm10'])
    if pm10_data <= 50:
        print("Currently,the air quality is safe")
    elif pm10_data > 50 and pm10_data <= 100:
        print("Currently,the air quality is safe to the general public. However, people who are sensitive to pollution may experience mild health effects")
    elif pm10_data > 100 and pm10_data <= 150:
        print("Currently,the air quality is safe to the general public. However, people who are sensitive to pollution may experience more serious health effects")
    elif pm10_data > 150 and pm10_data <= 200:
        print("Currently,the air quality is unhealthy. The general public may experience mild health effects")
    elif pm10_data > 200 and pm10_data <= 300:
        print("Currently,the air quality is very unhealthy. The general public may experience mild health effects")
    else:
        print("Currently,the air quality is hazardous. The general public may experience serious health effects")

    print("Right now the average pm10 data is: " + str(avg_pm10_data[0]['avg_pm10'])+"\n")
    print("Right now the average weather is: " + str(avg_pm10_data[0]['avg_weather'])+"\n")
    print("The current weather is: " + str(weather_results['results'][0]['temp']['value']) + "F")

def main():
    sample_job_every_120s()

if __name__ == "__main__":
    tl.start(block=True)
    main()

