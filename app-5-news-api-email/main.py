import requests

api_key = "51ce0f33e36a49dea88919950004b0f4"
url = "https://newsapi.org/v2/everything?q=apple&"\
    "from=2024-01-20&to=2024-01-20&sortBy=popularity&"\
    "apiKey=51ce0f33e36a49dea88919950004b0f4"

request = requests.get(url)
content =request.json()
print(content["totalResults"])
body = ""
for article in content["articles"]:
    if article["title"] is not None:
         body = body + article["title"]+"\n"+article["description"]+ "\n"

body =body.encode("utf-8")
