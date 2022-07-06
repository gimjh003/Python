import requests

class FlightSearch:
    def __init__(self):
        self.QUERY = "https://tequila-api.kiwi.com/locations/query"
        self.KEY = "{AUTO_CENSORED_BY_GITHUB}"
    def get(self, city):
        headers = {
            "apikey":self.KEY,
        }
        params = {
            "term":city,
            "location_types":"city"
        }
        res = requests.get(self.QUERY, params=params, headers=headers).json()["locations"][0]
        return res["code"]