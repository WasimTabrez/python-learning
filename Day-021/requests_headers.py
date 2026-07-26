import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

headers = {
    "User-Agent": "Python-Learning",
    "Accept": "application/json"
}

response = requests.get(url, headers=headers)

print("Status Code :", response.status_code)
print(response.json())
