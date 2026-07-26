import requests

try:

    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        timeout=5
    )

    print("Request Successful")
    print(response.status_code)

except requests.exceptions.Timeout:

    print("Request Timed Out")
