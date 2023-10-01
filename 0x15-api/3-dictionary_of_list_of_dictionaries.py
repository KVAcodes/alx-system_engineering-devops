#!/usr/bin/python3
"""Using what I did in task #0 I'm using this script to export data
in the JSON format.
"""
import json
import requests


if __name__ == '__main__':
    with (
        requests.get(f'https://jsonplaceholder.typicode.com/users')
    ) as user_json:
        with (
            requests.get(
                f'https://jsonplaceholder.typicode.com/todos'
            )
        ) as todos_json:
            users = json.loads(user_json.text)
            todos = json.loads(todos_json.text)
            with open(f"todo_all_employees.json", 'w') as json_file:
                data = {
                    f"{user['id']}": [{
                        "username": f"{user['username']}",
                        "task": f"{todo['title']}",
                        "completed": todo['completed']
                        } for todo in todos if user['id'] == todo['userId']]
                    for user in users
                }
                json.dump(data, json_file)
