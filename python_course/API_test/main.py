from email.mime.text import MIMEText
import smtplib
from time import sleep
import requests
import secret
import datetime as dt

data = requests.get("http://api.open-notify.org/iss-now.json").json()
position = (float(data["iss_position"]["latitude"]), float(data["iss_position"]["longitude"]))

params = {
    "lat":secret.MY_POSITION[0],
    "lng":secret.MY_POSITION[1],
    "formatted":0
}

data2 = requests.get("https://api.sunrise-sunset.org/json", params=params).json()
sunrise = int(data2["results"]["sunrise"].split('T')[1].split(':')[0])+7
sunset = int(data2["results"]["sunset"].split('T')[1].split(':')[0])+7

if sunrise>=24: sunrise = sunrise-24
if sunset>=24: sunrise = sunrise-24
current_time = dt.datetime.now().hour

def send_message():
    if current_time<=sunrise and current_time>=sunset:
        if secret.MY_POSITION[0]-5 <= position[0] <= secret.MY_POSITION[0]+5 and secret.MY_POSITION[1]-5 <= position[1] <= secret.MY_POSITION[1]+5:
            with smtplib.SMTP("smtp.naver.com") as connection:
                connection.starttls()
                connection.login("{AUTO_CENSORED_BY_GITHUB}", "{AUTO_CENSORED_BY_GITHUB}")
                msg = MIMEText("ISS is on your sky!")
                msg["Subject"] = "Look the sky!"
                msg["From"] = "{AUTO_CENSORED_BY_GITHUB}"
                msg["To"] = "{AUTO_CENSORED_BY_GITHUB}"
                connection.sendmail("{AUTO_CENSORED_BY_GITHUB}", "{AUTO_CENSORED_BY_GITHUB}", msg.as_string())

while True:
    send_message()
    sleep(60)