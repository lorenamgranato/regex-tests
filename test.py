import json


def test_json_format():
    try:
        with open("classifier.json") as json_file:
            json.load(json_file)
    except Exception as error:
        print("Json not properly formatted.")
        print(error)
        assert False
