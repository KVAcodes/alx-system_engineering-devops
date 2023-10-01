#!/usr/bin/python3
""" a Python script that, using this https://jsonplaceholder.typicode.com/
, for a given employee ID, returns information about his/her TODO list
progress."""
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
            total_tasks = len(todos)
            no_tasks_completed = sum(
                1 for todo in todos if todo['completed'] is True
            )
            print(
                f"Employee {user['name']} is done with tasks"
                f"({no_tasks_completed}/{total_tasks}):"
            )
            for todo in todos:
                if todo['completed'] is True:
                    print(f"\t {todo['title']}")
