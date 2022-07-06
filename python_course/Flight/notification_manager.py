from email.mime.text import MIMEText
import smtplib


class NotificationManager:
    def __init__(self):
        self.addr = "{AUTO_CENSORED_BY_GITHUB}"
        self.pwd = "{AUTO_CENSORED_BY_GITHUB}"
    def send(self, data, emails):
        with smtplib.SMTP("smtp.naver.com") as connection:
            connection.starttls()
            connection.login(self.addr, self.pwd)
            text = f"Low price alert! Only £{data['price']} to fly from {data['from']} to {data['to']}, from {data['start']} to {data['end']}."
            text += f"\n\nhttps://www.google.co.uk/flights?hl=en#flt={data['from']}.{data['to']}.{data['start']}*{data['to']}.{data['from']}.{data['end']}"
            msg = MIMEText(text)
            msg["Subject"] = "Low price alert!"
            msg["From"] = self.addr
            for email in emails:
                msg["To"] = email
                connection.sendmail(from_addr=self.addr, to_addrs=email, msg=msg.as_string())