#!/usr/bin/python3
"""Using what I did in task #0 I'm using this script to export data
in the JSON format.
"""
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
            with open(f"{id}.json", 'w') as json_file:
                data = {
                    f"{id}": [{
                        "task": f"{todo['title']}",
                        "completed": todo['completed'],
                        "username": f"{user['username']}"
                        } for todo in todos]
                }
                json.dump(data, json_file)
