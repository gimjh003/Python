import datetime as dt
import requests

SHEETY_ENDPOINT = "{CENSORED_BY_GITHUB}"
SHEETY_TOKEN = "{CENSORED_BY_GITHUB}"
NUTRITIONIX_ENDPOINT = "{CENSORED_BY_GITHUB}"
NUTRITIONIX_ID = "{CENSORED_BY_GITHUB}"
NUTRITIONIX_KEY = "{CENSORED_BY_GITHUB}"

query = input("Tell me which exercise you did : ")

headers = {
    "x-app-id":NUTRITIONIX_ID,
    "x-app-key":NUTRITIONIX_KEY,
    "Content-Type":"application/json"
}

data = {
    "query":query,
    "gender":"{CENSORED_BY_GITHUB}",
    "weight_kg": "{CENSORED_BY_GITHUB}",
    "age":"{CENSORED_BY_GITHUB}"
}

res = requests.post(NUTRITIONIX_ENDPOINT, json=data, headers=headers).json()

headers = {
    "Authorization":SHEETY_TOKEN
}

for result in res["exercises"]:
    time = dt.datetime.now()
    data = {
        "workout":{
            "date":time.strftime("%d/%m/%Y"),
            "time":time.strftime("%H:%M:%S"),
            "exercise":result["name"].title(),
            "duration":result["duration_min"],
            "calories":result["nf_calories"]
        }
    }
    requests.post(SHEETY_ENDPOINT, json=data, headers=headers)