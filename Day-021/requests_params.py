import requests

url = "https://jsonplaceholder.typicode.com/comments"

params = {
    "postId": 1
}

response = requests.get(url, params=params)

print("Requested URL:")
print(response.url)

print()

for comment in response.json()[:3]:
    print(comment["email"])
