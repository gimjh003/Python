import requests
import os

API_endpoint = "https://api.openweathermap.org/data/2.5/onecall"

params = {
    "lat":"{CENSORED_BY_GITHUB}",
    "lon":"{CENSORED_BY_GITHUB}",
    "units":"metric",
    "exclude":"current,minutely,daily,alerts",
    "appid":"{CENSORED_BY_GITHUB}",
}

res = requests.get(API_endpoint, params=params).json()

weathers = [_["weather"][0]["id"] for _ in res["hourly"][:12]]

rain = False
for _ in weathers:
    if _<700:
        rain = True
if rain:
    print("bring an umbrella.")

print(os.environ.get("USERNAME"))

# $ export OWM_API_KEY=keywithnoquotations; export ANOTHER_KEY=anotherkeywithnoquotations; python main.py