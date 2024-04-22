#!/usr/bin/python3
"""
project api task 1
"""
import csv
import requests
import sys


def get_employee(user_id):
    """
    Obtains and displays information about an employee's tasks.
    """
    user = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos = f"https://jsonplaceholder.typicode.com/todos/?userId={user_id}"

    name = requests.get(user).json().get("name")
    request_todo = requests.get(todos).json()

    csv_format = [["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                   "TASK_TITLE"]]

    for task in request_todo:
        csv_format.append([user_id, name, task.get('completed'),
                           task.get('title')])

    filename = f"{user_id}.csv"

    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL, quotechar='"')
        writer.writerows(csv_format[1:])


if __name__ == "__main__":
    if len(sys.argv) == 2:
        get_employee(sys.argv[1])
