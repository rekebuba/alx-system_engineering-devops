#!/usr/bin/python3
"""
from task #0, extended Python script to export data in the JSON format.
"""

import json
import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"


if __name__ == '__main__':
    result = {}
    for id in range(1, 11):
        username = requests.get(users_url + f"/{id}").json()['username']
        status = list(
            filter(
                lambda x: x['userId'] == id, requests.get(todos_url).json()
            )
        )

        for value in status:
            value['task'] = value.pop('title')
            value['username'] = username
            del value['id'], value['userId']

        result[id] = status

    with open('todo_all_employees.json', 'w') as file:
        json.dump(result, file)
