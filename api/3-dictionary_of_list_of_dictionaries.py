#!/usr/bin/python3

"""
This script can export a JSON file with tasks for all employees.

Needs:
    - The requests module
"""
import json
import requests

if __name__ == "__main__":

    # URLs to get users and todos data
    users_url = "https://jsonplaceholder.typicode.com/users"
    
    # Fetch users data
    users_response = requests.get(users_url)
    if users_response.status_code != 200:
        print(f"Error: Users data could not be fetched.")
        exit(1)

    users_data = users_response.json()

    # Prepare the dictionary to store all tasks by employee
    all_tasks = {}

    # Loop through each user and get their tasks
    for user in users_data:
        user_id = user['id']
        username = user['username']
        todos_url = (
            f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
        )

        # Fetch todos data for each user
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Store tasks for the current user in the dictionary
        tasks = [
            {
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            }
            for task in todos_data
        ]

        # Add the tasks list to the dictionary with user_id as the key
        all_tasks[user_id] = tasks

    # Write the JSON data to the file
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(all_tasks, jsonfile, indent=4)

    print(f"JSON file todo_all_employees.json has been created.")
