#!/usr/bin/python3
import requests
import sys

def fetch_todo_list(employee_id):
    url_user = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    url_todos = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    
    user_response = requests.get(url_user)
    todos_response = requests.get(url_todos)
    
    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Error: Unable to fetch data")
        return
    
    user = user_response.json()
    todos = todos_response.json()
    
    employee_name = user.get("name")
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]
    number_of_done_tasks = len(done_tasks)
    
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
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
