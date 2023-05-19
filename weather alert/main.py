import requests
import os

API_KEY = os.environ["WEATHER_API_KEY"]
CITY = os.environ["CITY"]
parameters = {"q": CITY, "appid": API_KEY}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

is_cloudy = False
for i in weather_data["list"][:12]:
    if i["weather"][0]["main"] == "Clouds":
        is_cloudy = True
        break

if is_cloudy:
    print("Cloudy")
else:
    print("Not cloudy")
