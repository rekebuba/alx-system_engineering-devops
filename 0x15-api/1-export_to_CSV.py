#!/usr/bin/python3
"""
Using from task #0, extended Python script to export data in the CSV format.
"""
import csv
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

    with open(f'{id}.csv', 'w') as file:
        csv_writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for value in status:
            csv_writer.writerow(
                [id, username, value['completed'], value['title']]
            )
