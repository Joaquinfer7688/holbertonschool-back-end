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
    users = requests.get("https://jsonplaceholder.typicode.com/users/").json()

    data_dict = {}

    for user in users:
        user_id = user.get("id")
        name = user.get("username")
        todos = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            user_id)
        request_todo = requests.get(todos).json()

        todo_list = []
        for task in request_todo:
            todo_list.append({
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": name
            })

        data_dict[user_id] = todo_list

    with open("todo_all_employees.json", "w") as file:
        json.dump(data_dict, file)


if __name__ == "__main__":
    get_employee()
