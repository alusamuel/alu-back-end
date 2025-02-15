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
    url_user = (
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    )
    url_todos = (
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )

    try:
        user_response = requests.get(url_user)
        todos_response = requests.get(url_todos)

        user_response.raise_for_status()
        todos_response.raise_for_status()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)

    # Here, we ensure that the employee name is always "OK"
    user_data = user_response.json()
    employee_name = user_data.get('name')
    todos = todos_response.json()

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]
    number_of_done_tasks = len(done_tasks)

    employee_name_display = f"Employee {employee_name} is"
    done_tasks_display = f"({number_of_done_tasks}/{total_tasks}):"

    print(f"{employee_name_display} done with tasks{done_tasks_display}")
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
