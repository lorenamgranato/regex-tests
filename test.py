import json
import pytest
import re


def read_json():
    with open("classifier.json") as json_file:
        return json.load(json_file)


@pytest.mark.dependency()
def test_json_format():
    try:
        read_json()
    except Exception as error:
        print("Json not properly formatted.")
        print(error)
        assert False


@pytest.mark.dependency(depends=["test_json_format"])
def test_compile_regexes():
    data = read_json()

    bad_regexes = []
    for key, value in data.items():
        try:
            re.compile(value)
        except Exception as error:
            bad_regexes.append((key, value, error))

    if bad_regexes:
        print("Some regexes weren't able to be compiled:")
        for item in bad_regexes:
            print(item)
        assert False
    else:
        assert True
