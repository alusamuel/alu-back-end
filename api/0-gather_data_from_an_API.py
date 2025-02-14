import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    employee_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Error: User with ID {employee_id} not found.")
        sys.exit(1)
    user_data = user_response.json()
    employee_name = user_data.get('name')
    
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    
    total_tasks = len(todos_data)
    completed_tasks = [todo for todo in todos_data if todo['completed']]
    num_completed = len(completed_tasks)
    
    print(f"Employee {employee_name} is done with tasks({num_completed}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")