import requests

city = input("Enter city: ")

url = f"https://wttr.in/{city}?format=j1"

response = requests.get(url)

weather = response.json()

current = weather["current_condition"][0]

print("Temperature :", current["temp_C"], "°C")
print("Humidity :", current["humidity"], "%")
print("Weather :", current["weatherDesc"][0]["value"])
