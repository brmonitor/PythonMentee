# Python Mentee - Level 3 - Exercises
# https://bairesdev.atlassian.net/servicedesk/customer/article/2101576225
# 5  - Write a Python program that reads a JSON object from a file, sorts the object keys in ascending order,
#       then writes the JSON object back into the file.

import json, os


def create_json_file():
    data_unordered_dic = {
        "dic2": {
            "h": 8,
            "g": 7,
            "f": 6,
            "e": 5
        },
        "dic1": {
            "d": 4,
            "c": 3,
            "b": 2,
            "a": 1
        }
    }
    if os.path.exists("data_file.json"):
        os.remove("data_file.json")

    with open("data_file.json", "w") as write_file:
        json.dump(data_unordered_dic, write_file)


def read_json_file():
    with open("data_file.json", "r") as file:
        data = json.load(file)
        return data


def write_sorted_json_file(data_unordered_dic):
    with open("data_file.json", "w") as write_file:
        json.dump(data_unordered_dic, write_file, sort_keys=True)


if __name__ == '__main__':
    create_json_file()
    data = read_json_file()
    print('Unordered object : ', data)
    write_sorted_json_file(data)
    print('Ordered object   : ', read_json_file())
