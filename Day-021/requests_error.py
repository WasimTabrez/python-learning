import requests

url = "https://jsonplaceholder.typicode.com/invalid"

try:

    response = requests.get(url)

    response.raise_for_status()

    print(response.json())

except requests.exceptions.HTTPError as error:

    print("HTTP Error")
    print(error)

except requests.exceptions.RequestException as error:

    print(error)
