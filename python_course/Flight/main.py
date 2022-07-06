from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

sheet_manager = DataManager()
flight_search = FlightSearch()
flight_data = FlightData()
notification_manager = NotificationManager()

sheet_data = sheet_manager.get()["prices"]

# sheet_manager.register()
mails = sheet_manager.email()

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        code = flight_search.get(row["city"])
        row["iataCode"] = code
        sheet_manager.put(row)

else:
    for row in sheet_data[:2]:
        data = flight_data.get(row["iataCode"])
        if not data:
            print("Can't find ticket.")
        elif row["lowestPrice"] > data["price"]:
            notification_manager.send(data, mails)
        else:
            print("There isn't low price ticket.")