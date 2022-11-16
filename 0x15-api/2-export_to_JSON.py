#!/usr/bin/python3
"""Exports a user TODO list as a CSV file
From https://jsonplaceholder.typicode.com/users/1/todos
"""
import json
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
        json_data = [
            {
                "task": todo.get('title'),
                "completed": todo.get('completed'),
                "username": user.get('username')
            }
            for todo in todos]

        # Write data to file
        with open('{}.json'.format(user_id), 'w') as json_file:
            json.dump({user_id: json_data}, json_file)
