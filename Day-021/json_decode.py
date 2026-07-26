import json

json_data = '''
{
    "id": 101,
    "name": "Wasim",
    "course": "Python",
    "marks": 95
}
'''

student = json.loads(json_data)

print(student)
print(student["name"])
