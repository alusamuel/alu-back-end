#!/usr/bin/python3

"""
This script can export a JSON file with tasks for all employees.

Needs:
    - The requests module
"""
import json
import requests

if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users = requests.get(users_url).json()
    todos = requests.get(todos_url).json()

    user_dict = {user['id']: user['username'] for user in users}

    result = {}
    for todo in todos:
        user_id = todo['userId']
        if str(user_id) not in result:
            result[str(user_id)] = []
        result[str(user_id)].append({
            "username": user_dict[user_id],
            "task": todo['title'],
            "completed": todo['completed']
        })

    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(result, jsonfile)
