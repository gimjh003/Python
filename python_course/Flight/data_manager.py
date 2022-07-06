import requests

class DataManager:
    def __init__(self):
        self.GET = "{AUTO_CENSORED_BY_GITHUB}"
        self.PUT = "{AUTO_CENSORED_BY_GITHUB}"
        self.MAIL = "{AUTO_CENSORED_BY_GITHUB}"
    def get(self):
        return requests.get(self.GET).json()
    def put(self, data):
        requests.put(self.PUT.format(data["id"]), json={"price":data})
    def email(self):
        res = requests.get(self.MAIL).json()["users"]
        return [_["email"] for _ in res]
    def register(self):
        f_name = input("Welcome to flight club.\nWe find the best flight deals and email you.\nWhat is your first name?\n")
        l_name = input("What is your last name?\n")
        mail = input("What is your email?\n")
        mail_c = input("Type your email again.\n")
        if mail != mail_c:
            print("Register failed.")
            return
        data = {
            "user":{
                "firstName":f_name,
                "lastName":l_name,
                "email":mail
            }
        }
        requests.post(self.MAIL, json=data)