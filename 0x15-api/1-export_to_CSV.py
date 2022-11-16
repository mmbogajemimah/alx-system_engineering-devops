#!/usr/bin/python3
"""Exports a user TODO list as a CSV file
From https://jsonplaceholder.typicode.com/users/1/todos
"""
import requests
import sys

# Disable module execution, only run directly
if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Get command arguments
        user_id = sys.argv[1]

        # Enpoints urls
        api_url = 'https://jsonplaceholder.typicode.com/'
        user_url = api_url + 'users/{}'.format(user_id)
        user_todos_url = api_url + 'users/{}/todos'.format(user_id)

        # Request data
        user = requests.get(user_url).json()
        todos = requests.get(user_todos_url).json()

        # Process data
        csv_data = ['"{}","{}","{}","{}"'.format(
            user_id,
            user.get('username'),
            todo.get('completed'),
            todo.get('title')) for todo in todos]

        # Write data to file
        with open('{}.csv'.format(user_id), 'w') as csv_file:
            csv_file.write('\n'.join(csv_data))
