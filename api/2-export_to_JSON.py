#!/usr/bin/python3
"""
project api task 2
"""
import requests
import sys
import json


def get_employee(user_id):
    """
    export data in the JSON format.
    """
    user_id = sys.argv[1]
    user = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todos = "https://jsonplaceholder.typicode.com/todos/?userId={}".format(
        user_id)
    name = requests.get(user).json().get("name")
    request_todo = requests.get(todos).json()

    todo_list = []

    for task in request_todo:
        todo_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": name
        })

    result = {name: todo_list}

    with open(f"{user_id}.json", "w") as file:
        json.dump(result, file)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        get_employee(sys.argv[1])
