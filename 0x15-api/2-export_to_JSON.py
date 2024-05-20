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
    id = int(sys.argv[1])
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

    result = {id: status}

    with open(f'{id}.json', 'w') as file:
        json.dump(result, file)
