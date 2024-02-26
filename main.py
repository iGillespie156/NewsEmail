import requests
import os


key = os.getenv("NEWSAPIKEY")

print(key)

url = f"https://newsapi.org/v2/everything?q=tesla&from=2024-01-26&sortBy=publishedAt&apiKey=" \
      f"{key}"

request = requests.get(url)

content = request.json()
for article in content["articles"]:
      print(article["title"])
      print(article["description"])
