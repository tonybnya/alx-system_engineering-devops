#!/usr/bin/python3
# Author: @tonybnya
"""
This Python script uses 0-gather_data_from_an_API.py file,
and export data in the JSON format.
"""
import json
import requests


if __name__ == "__main__":
    URL = 'https://jsonplaceholder.typicode.com/'

    users_url = URL + 'users'
    tasks_url = URL + 'todos'

    users = requests.get(users_url).json()
    all_tasks = requests.get(tasks_url).json()

    obj = {}

    for user in users:
        id_ = user.get("id")
        name = user.get("username")
        tasks = list(filter(lambda x: x.get("userId") == id_, all_tasks))

        data = list(map(
            lambda x: {
                "username": name,
                "task": x.get("title"),
                "completed": x.get("completed")
            },
            tasks
        ))

        obj["{}".format(id_)] = data

    with open("todo_all_employees.json" "w") as file:
        json.dump(obj, file)
