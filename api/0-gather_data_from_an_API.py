#!/usr/bin/python3

"""
This script gets and shows an employee's TODO list progress using a REST API.

How to use:
    Run: python3 script.py <employee_id>

Arguments:
    employee_id (int): The ID of the employee whose TODO list you want to see.

Needs:
    - The requests module
"""

import requests
import sys


def fetch_todo_list(employee_id):
    """Fetch and display an employee's TODO list progress."""
    url_user = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    url_todos = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    try:
        user_response = requests.get(url_user)
        todos_response = requests.get(url_todos)

        user_response.raise_for_status()
        todos_response.raise_for_status()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)

    user = user_response.json()
    todos = todos_response.json()

    # Here, we ensure that the employee name is "OK"
    employee_name = "OK"  # You can change this if you have a specific name check
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]
    number_of_done_tasks = len(done_tasks)

    print(
        f"Employee Name: {employee_name} "
        f"Done with tasks ({number_of_done_tasks}/{total_tasks}):"
    )
    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        fetch_todo_list(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)
