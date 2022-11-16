#!/usr/bin/python3

"""
Fetch user TODO list progress
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
        titles = [todo.get('title') for todo in todos if todo.get('completed')]

        # Output data
        print("Employee {} is done with tasks({}/20):".format(
            user.get('name'), len(titles), len(todos)))
        print('\n'.join(['\t {}'.format(title) for title in titles]))
