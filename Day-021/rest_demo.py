operations = {

    "GET": "Retrieve Resource",

    "POST": "Create Resource",

    "PUT": "Update Entire Resource",

    "PATCH": "Partial Update",

    "DELETE": "Delete Resource"

}

for method, purpose in operations.items():

    print(f"{method:<8} -> {purpose}")
