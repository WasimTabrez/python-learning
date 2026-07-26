import requests

username = input("GitHub Username: ")

url = f"https://api.github.com/users/{username}"

response = requests.get(url)

if response.status_code == 200:

    user = response.json()

    print("Name :", user["name"])
    print("Public Repositories :", user["public_repos"])
    print("Followers :", user["followers"])
    print("Following :", user["following"])

else:

    print("User Not Found")
