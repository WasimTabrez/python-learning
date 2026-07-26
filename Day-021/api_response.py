import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)

user = response.json()

print("Name :", user["name"])
print("Username :", user["username"])
print("Email :", user["email"])
print("City :", user["address"]["city"])
