# Python Mentee - Level 5 - Exercises
# https://bairesdev.atlassian.net/servicedesk/customer/article/2101576225
# 1a - Create a simple function that fetches and parses the JSON from this API:
#       https://jsonplaceholder.typicode.com/todos/ and then print all the completed TODOs in the screen.

import urllib.request
import requests


def fetch_json(page):
    with urllib.request.urlopen(page) as response:
        html = response.read()
        print(html)


def fetch_json2(page):
    lis = requests.get(page).json()

    # conventional solution
    # for d in lis:
    #     if d['completed']:
    #         print(d)

    # using list comprehension
    [print(d) for d in lis if d['completed']]


if __name__ == '__main__':
    fetch_json2('https://jsonplaceholder.typicode.com/todos/')
