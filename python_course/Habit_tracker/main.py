import datetime as dt
import requests

PIXELA_ENDPOINT = "{CENSORED_BY_GITHUB}"
USERNAME = "{CENSORED_BY_GITHUB}"
TOKEN = "{CENSORED_BY_GITHUB}"
GRAPH_ID = "{CENSORED_BY_GITHUB}"

user_data = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

res = requests.post(PIXELA_ENDPOINT, json=user_data)
print(res.text)

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_config = {
    "id": GRAPH_ID,
    "name": "study",
    "unit": "min",
    "type": "int",
    "color": "momiji"
}

res = requests.post(GRAPH_ENDPOINT, json=graph_config, headers=headers)
print(res.text)

quantity = 100
today = dt.datetime.now().strftime("%Y%m%d")

data = {
    "date": today,
    "quantity": str(quantity)
}

res = requests.post(f"{GRAPH_ENDPOINT}/{GRAPH_ID}", json=data, headers=headers)
print(res.text)

new_quantity = quantity+20
select = dt.datetime(year=2022, month=7, day=3).strftime("%Y%m%d")

data = {
    "quantity": str(new_quantity),
}
res = requests.put(f"{GRAPH_ENDPOINT}/{GRAPH_ID}/{select}", headers=headers, json=data)
print(res.text)


# res = requests.delete(f"{GRAPH_ENDPOINT}/{GRAPH_ID}/{select}", headers=headers)
# print(res.text)