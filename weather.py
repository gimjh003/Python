import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/search?q=%EB%82%A0%EC%94%A8&oq=%EB%82%A0%EC%94%A8&aqs=chrome..69i57j69i61j69i60j69i61.1718j0j4&sourceid=chrome&ie=UTF-8"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
weather = soup.find("span", attrs={"id":"wob_tm"}).get_text()
print("현재 기온은 섭씨 {0}도 입니다.".format(weather))