import requests
from dateutil import tz
import datetime as dt

iss_info = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_info.raise_for_status()
iss_info = iss_info.json()
ISS_LAT = float(iss_info["iss_position"]["latitude"])
ISS_LNG = float(iss_info["iss_position"]["longitude"])
LAT = 35.689487
LNG = 139.691711

parameters = {"lat": LAT, "lng": LNG, "formatted": 1}
sunrise_info = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
sunrise_info.raise_for_status()
sunrise_info = sunrise_info.json()
sunrise = sunrise_info["results"]["sunrise"]
sunset = sunrise_info["results"]["sunset"]
sunset_hour = int(sunset.split(":")[0])

timezone = tz.gettz() 
date = str(dt.datetime.now(tz=timezone))
now_hour = int(date.split(" ")[1].split(":")[0])

if int(ISS_LAT) < 40 and int(ISS_LAT) > 35 and int(ISS_LNG) < 144 and int(ISS_LNG) > 134 and sunset_hour == now_hour:
    print("Look Up!")
    