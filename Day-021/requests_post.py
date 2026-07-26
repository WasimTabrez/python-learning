import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "Python",
    "body": "Learning Backend Development",
    "userId": 1
}

response = requests.post(
    url,
    json=data
)

print("Status :", response.status_code)
print()

print(response.json())
