import requests

params = {
    "amount":10,
    "category":18,
    "type":"boolean",
}

res = requests.get("https://opentdb.com/api.php", params=params)
res.raise_for_status()
data = res.json()

question_data = data["results"]