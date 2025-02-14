#!/usr/bin/python3

"""
This script can export a CSV file.

Needs:
    - The requests module
"""
import csv
import requests
import sys

if __name__ == "__main__":
    # Check if the correct number of arguments is passed
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    # Get employee ID from command line argument
    employee_id = sys.argv[1]

    # URLs to get user and todos data
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = (
        f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    )

    # Fetch user data
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Error: User with ID {employee_id} not found.")
        sys.exit(1)

    # Extract username from user data
    user_data = user_response.json()
    username = user_data.get('username')

    # Fetch todos data
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Create CSV file and write the header
    with open(f"{employee_id}.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        # Write the header of the CSV file
        writer.writerow([
            "USER_ID", 
            "USERNAME", 
            "TASK_COMPLETED_STATUS", 
            "TASK_TITLE"
        ])

        # Write the tasks for the user
        for task in todos_data:
            # Write each task in the required format
            writer.writerow([employee_id, username, task['completed'], task['title']])

    print(f"CSV file {employee_id}.csv has been created.")
