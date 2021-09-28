import json


def read_json():
    with open("classifier.json") as json_file:
        return json.load(json_file)


def test_json_format():
    try:
        read_json()
    except Exception as error:
        print("Json not properly formatted.")
        print(error)
        assert False
