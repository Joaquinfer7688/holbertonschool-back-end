#!/usr/bin/python3
"""
project api task 3
"""
import json
import requests


def get_employee():
    """
    export data in the JSON format.
    """
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()

    data_dict = {}

    for user in users:
        user_id = user.get("id")
        request_todo = requests.get(
            f"https://jsonplaceholder.typicode.com/todos/?userId={user_id}"
         ).json()

        todo_list = []
        for task in request_todo:
            todo_list.append({
                "username": user.get("username"),
                "task": task.get("title"),
                "completed": task.get("completed")
            })

        data_dict[user_id] = todo_list

    with open("todo_all_employees.json", mode="w") as file:
        json.dump(data_dict, file)


if __name__ == "__main__":
    get_employee()
