#!/usr/bin/python3
"""
project api task 2
"""
import json
import requests
import sys


def get_employee(user_id):
    """
    export data in the JSON format.
    """
    user = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos = f"https://jsonplaceholder.typicode.com/todos/?userId={user_id}"
    user = requests.get(user).json()
    request_todo = requests.get(todos).json()

    todo_list = []

    for task in request_todo:
        todo_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")
        })

    result = {user_id: todo_list}

    with open(f"{user_id}.json", mode="w") as file:
        json.dump(result, file)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        get_employee(sys.argv[1])
