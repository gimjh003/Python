import datetime as dt
import random
from email.mime.text import MIMEText
import smtplib
import pandas

MY_EMAIL = "three@three.three"
MY_PASSWORD = "[CENSORED]"

now = dt.datetime.now()
friends = pandas.read_csv("python_course/SMTP/birthday.csv").to_dict(orient="records")

def send_happy_birthday(friend):
    with smtplib.SMTP("smtp.naver.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        with open("python_course/SMTP/template.txt", encoding="UTF8") as template:
            letter = template.read().replace("[NAME]", friend["name"])
            msg = MIMEText(letter)
            msg["Subject"] = "Happy Birthday!!!"
            msg["From"] = MY_EMAIL
            msg["To"] = friend["email"]
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=friend["email"], msg=msg.as_string())

for friend in friends:
    if friend["month"] == now.month and friend["day"] == now.day:
        send_happy_birthday(friend)

# TO_EMAIL = "blah@blah.blah"

# now = dt.datetime.now()
# now = now.weekday()

# def generate_quote():
#     quote = ""
#     with open("python_course/SMTP/quotes.txt") as file:
#         data = file.read().split('\n')
#         quote = random.choice(data)
#     return quote

# if now==0:
#     with smtplib.SMTP("smtp.naver.com") as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         msg = MIMEText(generate_quote())
#         msg["Subject"] = "Happy monday!"
#         msg["From"] = MY_EMAIL
#         msg["To"] = TO_EMAIL
#         connection.sendmail(from_addr=MY_EMAIL, to_addrs=TO_EMAIL, msg=msg.as_string())