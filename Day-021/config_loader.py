import json

config = {
    "base_url": "https://jsonplaceholder.typicode.com",
    "timeout": 10,
    "api_version": "v1"
}

with open("config.json", "w") as file:
    json.dump(config, file, indent=4)

with open("config.json") as file:
    settings = json.load(file)

print(settings)
