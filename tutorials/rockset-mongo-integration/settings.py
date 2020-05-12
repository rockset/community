import os
from dotenv import load_dotenv
import requests

load_dotenv()
MONGO_URI = os.environ.get('MONGO_URI')
WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
AIR_QUALITY = os.environ.get('AIR_QUALITY')
ROCKSET_API_KEY= os.environ.get('ROCKSET_API_KEY')

# import requests, json

# def executeLambda():
#   r = requests.post('https://api.rs2.usw2.rockset.com/v1/orgs/self/ws/commons/lambdas/getLatPositionJOIN/versions/2',
#   headers={'Authorization': 'ApiKey API_KEY'})
#   return r.json()
