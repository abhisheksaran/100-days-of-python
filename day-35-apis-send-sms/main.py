import os
import requests

LAT = 28.704060  # Your latitude
LON = 77.102493  # Your longitude
API_KEY = os.environ.get("OPENWEATHER_API_KEY")
ENDPOINT = f"https://api.openweathermap.org/data/2.5/onecall?lat={LAT}&lon={LON}&appid={API_KEY}"

response = requests.get(ENDPOINT)
response = response.json()

will_rain = False
for hour_data in response['hourly'][:12]:
    if hour_data['weather'][0]['id'] < 700:
        will_rain = True
        break
if will_rain:
    print("it will rain today")
else:
    print("it won't rain today")