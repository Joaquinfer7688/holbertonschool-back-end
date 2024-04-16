#!/usr/bin/python3
"""
project api task 1
"""
import requests
import sys
import csv


def get_employee(user_id):
    """
    Obtains and displays information about an employee's tasks.
    """
    user_id = sys.argv[1]
    user = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todos = "https://jsonplaceholder.typicode.com/todos/?userId={}".format(
        user_id)
    name = requests.get(user).json().get("name")
    request_todo = requests.get(todos).json()

    filename = "{}.csv".format(user_id)
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        csv_format = [["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]]
    for task in request_todo:
        csv_format.append([user_id, name, task.get("completed"), task.get("title")])


if __name__ == "__main__":
    if len(sys.argv) == 2:
        get_employee(sys.argv[1])
