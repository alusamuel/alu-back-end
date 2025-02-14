#!/usr/bin/python3

"""
This script can export a JSON file.

Needs:
    - The requests module
"""
import json
import requests
import sys

if __name__ == "__main__":
    # Check if the correct number of arguments is passed
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Fetch user data
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Error: User with ID {employee_id} not found.")
        sys.exit(1)

    user_data = user_response.json()
    username = user_data.get('username')

    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Create JSON structure to hold tasks
    tasks = [
        {
            "task": task['title'],
            "completed": task['completed'],
            "username": username
        }
        for task in todos_data
    ]

    export_data = {employee_id: tasks}

    with open(f"{employee_id}.json", 'w') as jsonfile:
        json.dump(export_data, jsonfile, indent=4)

    print(f"JSON file {employee_id}.json has been created.")
