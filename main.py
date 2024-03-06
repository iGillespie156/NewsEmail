import requests
import os
from send_email import send_email
import datetime

date = datetime.date.today()
callday = datetime.timedelta(25)
final_date = date - callday

key = os.getenv("NEWSAPIKEY")

topic = "tesla"

url = f"https://newsapi.org/v2/everything?" \
      f"q={topic}" \
      f"&from={final_date}" \
      f"&sortBy=published" \
      f"At&apiKey={key}" \
      f"&language=en"

request = requests.get(url)

content = request.json()
body = ""


for article in content["articles"][:20]:
    if article["title"] is not None:
        body = body + article["title"] + '\n' + article["description"] \
               + '\n' + article["url"] + 2*'\n'


email = "Subject: Today's News" + "\n" + body
email = email.encode("utf-8")
send_email(email)
