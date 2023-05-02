#!/usr/bin/python3
# Author: @tonybnya
"""
This Python script uses 0-gather_data_from_an_API.py file,
and export data in the JSON format.
"""
import json
import requests
import sys


if __name__ == "__main__":
    URL = 'https://jsonplaceholder.typicode.com/'
    users_url = URL + 'users'
    users = requests.get(users_url).json()

    obj = {}

    for user in users:
        id_ = user.get("id")
        name = user.get("username")
        user_url = "{}/{}".format(users_url, id_)
        todos_url = "{}/todos/".format(user_url)
        tasks = requests.get(todos_url).json()

        obj[id_] = []

        for task in tasks:
            status = task.get("completed")
            title = task.get("title")

            obj[id_].append({
                "task": title,
                "completed": status,
                "username": name
            })

    with open("todo_all_employees.json" "w") as file:
        json.dump(obj, file)
