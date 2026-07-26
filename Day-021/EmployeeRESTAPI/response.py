import json


def response(status, data):

    return {

        "status": status,

        "body": json.dumps(

            data,

            indent=4

        )

    }
