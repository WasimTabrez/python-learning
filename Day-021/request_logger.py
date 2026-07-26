from datetime import datetime

url = "https://jsonplaceholder.typicode.com/posts"

with open("requests.log", "a") as file:

    file.write(
        f"{datetime.now()} -> GET {url}\n"
    )

print("Request Logged Successfully.")
