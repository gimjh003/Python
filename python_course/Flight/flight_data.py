from pprint import pprint
import requests
import datetime as dt

class FlightData:
    def __init__(self):
        self.QUERY = "https://tequila-api.kiwi.com/v2/search"
        self.KEY = "{AUTO_CENSORED_BY_GITHUB}"
    def get(self, city):
        today = dt.datetime.now()
        headers = {
            "apikey":self.KEY,
            "Content-Type":"application/json"
        }
        params = {
            "fly_from":"city:LON",
            "fly_to":f"city:{city}",
            "date_from":(today+dt.timedelta(1)).strftime("%d/%m/%Y"),
            "date_to":(today+dt.timedelta(180)).strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type":"round",
            "max_stopovers":0,
            "curr":"GBP"
        }
        try:
            res = requests.get(self.QUERY, params=params, headers=headers).json()["data"][0]
        except:
            params["max_stopovers"] = 1
            res = requests.get(self.QUERY, params=params, headers=headers).json()["data"]
            # There is no "data" key value
        else:
            data = {
                "from":res["route"][0]["cityFrom"]+"-"+res["route"][0]["flyFrom"],
                "to":res["route"][-1]["cityFrom"]+"-"+res["route"][-1]["flyFrom"],
                "start":res["route"][0]["local_departure"].split('T')[0],
                "end":res["route"][-1]["local_departure"].split('T')[0],
                "price":res["price"]
            }
            return data