import requests
import datetime as dt
import os


APP_ID = os.environ["APP_ID"]
APP_KEY = os.environ["APP_KEY"]

now = dt.datetime.now()
DATE = now.strftime("%d/%m/%Y")
TIME = now.strftime("%H:%M:%S")

parameters = {"query": input("What did you do today?: ")}
headers = {"x-app-id": APP_ID, "x-app-key": APP_KEY}
response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=parameters, headers=headers)
data = response.json()

activity = data["exercises"][0]["name"].title()
duration = data["exercises"][0]["duration_min"]
calories = data["exercises"][0]["nf_calories"]


USER_KEY = os.environ["USER_KEY"]
USER_ID = os.environ["USER_ID"]
endpoint = f"https://api.sheety.co/{USER_ID}/workout/workouts"
params = {"workout": {"date": DATE, "time": TIME, "exercise": activity, "duration (mins)": duration, "calories": calories}}
headers = {"Authorization": f"Bearer {USER_KEY}"}
resp = requests.post(url=endpoint, json=params, headers=headers)
print(resp.text)