#!/usr/bin/python3

"""
This script can export a CSV file.

Needs:
    - The requests module
"""
import requests
import sys
import csv

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)
    
    employee_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(
            f"Error: User with ID {employee_id} not found."
        )
        sys.exit(1)
    user_data = user_response.json()
    username = user_data.get('username')
    
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    
    with open(f"{employee_id}.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow(
                [employee_id, username, task['completed'], task['title']]
            )
