from email.mime.text import MIMEText
import smtplib
import requests
import datetime as dt

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "{AUTO_CENSORED_BY_GITHUB}"
NEWS_API_KEY = "{AUTO_CENSORED_BY_GITHUB}"

SMTP_USERNAME = "{AUTO_CENSORED_BY_GITHUB}"
SMTP_PASSWORD = "{AUTO_CENSORED_BY_GITHUB}"

TARGET_ADDR = "{AUTO_CENSORED_BY_GITHUB}"

news_form = """
Headline : [HEADLINE]
Brief : [BRIEF]
"""

stock_params = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "outputsize":"compact",
    "datatype":"json",
    "apikey":STOCK_API_KEY,
}

today = dt.datetime.now()
res = requests.get(STOCK_ENDPOINT, params=stock_params).json()
yt = dt.datetime.now() - dt.timedelta(1)
yt_str = yt.strftime("%Y-%m-%d")
byt_str = (yt-dt.timedelta(1)).strftime("%Y-%m-%d")

yt_closing_stock = float(res["Time Series (Daily)"][yt_str]["4. close"])
byt_closing_stock = float(res["Time Series (Daily)"][byt_str]["4. close"])

difference = abs(yt_closing_stock-byt_closing_stock)/yt_closing_stock*100

if yt_closing_stock-byt_closing_stock>0: symbol = '🔺'
else: symbol = '🔻'

def get_news():
    news_params = {
        "q":COMPANY_NAME,
        "searchIn":"title,description",
        "apiKey":NEWS_API_KEY,
    }
    res = requests.get(NEWS_ENDPOINT, params=news_params).json()
    column = res["articles"][:3]
    msg = ""
    for news in column:
        content = news_form.replace("[HEADLINE]", news["title"])
        content = content.replace("[BRIEF]", news["description"])
        msg = msg+content+"\n"
    return msg

def send_message(title):
    news = get_news()
    with smtplib.SMTP("smtp.naver.com") as connection:
        connection.starttls()
        connection.login(SMTP_USERNAME, SMTP_PASSWORD)
        msg = MIMEText(news)
        msg["Subject"] = title
        msg["From"] = SMTP_USERNAME
        msg["To"] = TARGET_ADDR
        connection.sendmail(SMTP_USERNAME, TARGET_ADDR, msg=msg.as_string())

if difference>=5:
    send_message(f"{STOCK_NAME} : {symbol} {difference:.3}%")