#!/usr/bin/python3
"""
project api task 0
"""
import requests
import sys


def get_employee():
    """
    Obtains and displays information about an employee's tasks.
    """
    user_id = sys.argv[1]
    user = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todos = "https://jsonplaceholder.typicode.com/todos/?userId={}".format(
        user_id)
    name = requests.get(user).json().get("name")
    request_todo = requests.get(todos).json()
    tasks_completed = [task.get("title") for
                       task in request_todo if task.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(name,
                                                          len(tasks_completed),
                                                          len(request_todo)))
    print("\n".join("\t {}".format(task) for task in tasks_completed))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        get_employee()
