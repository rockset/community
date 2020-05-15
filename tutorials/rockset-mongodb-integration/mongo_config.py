
from pymongo import MongoClient
from settings import MONGO_URI


client = MongoClient(MONGO_URI)
db = client.get_database("weather_pollution_db")
weather_data_collection = db.weather_data
pollution_data_collection = db.air_pollution_data
