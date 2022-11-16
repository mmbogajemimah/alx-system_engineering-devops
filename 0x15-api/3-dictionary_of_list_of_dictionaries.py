#!/usr/bin/python3
"""Exports all todos as a JSON file
From https://jsonplaceholder.typicode.com/users/1/todos
"""
import json
import requests
import sys

# Endpoints urls
api_url = 'https://jsonplaceholder.typicode.com/'
users_url = api_url + 'users'
todos_url = api_url + 'todos'


# Disable module execution, only run directly
if __name__ == "__main__":

    # Request users data
    users = requests.get(users_url).json()

    with open("todo_all_employees.json", "w") as json_file:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(api_url + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in users}, json_file)
