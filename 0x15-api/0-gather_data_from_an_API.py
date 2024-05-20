#!/usr/bin/python3
"""
A Python script that, using given REST API URL, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


url = "https://jsonplaceholder.typicode.com/"

if __name__ == "__main__":
    id = int(sys.argv[1])
    users = f"users/{id}/"
    todos = "todos/"

    name = requests.get(url + users).json()['name']
    result = requests.get(url + todos).json()
    total_tasks = list(filter(lambda x: x['userId'] == id, result))
    completed = list(filter(lambda x: x['completed'] is True, total_tasks))
    print(
        "Employee {} is done with tasks ({}/{}):".format(
            name,
            len(completed),
            len(total_tasks)
        )
    )

    for title in completed:
        print(f"\t {title['title']}")
