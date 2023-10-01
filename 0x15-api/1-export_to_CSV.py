#!/usr/bin/python3
"""Using what I did in task #0 I'm using this script to export data
in the CSV format.
"""
import csv
import json
import requests
import sys


if __name__ == '__main__':
    id = sys.argv[1]
    with (
        requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')
    ) as user_json:
        with (
            requests.get(
                f'https://jsonplaceholder.typicode.com/users/{id}/todos'
            )
        ) as todos_json:
            user = json.loads(user_json.text)
            todos = json.loads(todos_json.text)
            with open(f"{id}.csv", 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
                for todo in todos:
                    row_values = [f"{id}", f"{user['username']}",
                                  f"{todo['completed']}", f"{todo['title']}"]
                    csv_writer.writerow(row_values)
