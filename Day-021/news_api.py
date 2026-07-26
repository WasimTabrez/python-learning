import requests

API_KEY = "YOUR_API_KEY"

url = (
    f"https://newsapi.org/v2/top-headlines"
    f"?country=us&apiKey={API_KEY}"
)

response = requests.get(url)

if response.status_code == 200:

    data = response.json()

    for article in data["articles"][:5]:

        print(article["title"])

else:

    print("Invalid API Key or Request Failed")
