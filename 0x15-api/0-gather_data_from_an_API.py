#!/usr/bin/python3
"""
A Python script that, using given REST API URL, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"

if __name__ == "__main__":
    id = int(sys.argv[1])

    name = requests.get(users_url + f"/{id}").json()['name']
    result = requests.get(todos_url).json()
    total_tasks = list(filter(lambda x: x['userId'] == id, result))
    completed = list(filter(lambda x: x['completed'] is True, total_tasks))
    print(
        "Employee {} is done with tasks({}/{}):".format(
            name,
            len(completed),
            len(total_tasks)
        )
    )

    for title in completed:
        print(f"\t {title['title']}")
