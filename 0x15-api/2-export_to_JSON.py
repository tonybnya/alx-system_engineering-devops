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
    id_ = sys.argv[1]
    user_url = URL + 'users/' + id_
    tasks_url = URL + 'todos'

    user = requests.get(user_url).json()
    name = user.get('username')
    tasks = requests.get(tasks_url, params={"userId": id_}).json()

    obj = {id_: []}

    for task in tasks:
        status = task.get("completed")
        title = task.get("title")

        obj[id_].append({"task": title, "completed": status, "username": name})

    with open("{}.json".format(id_), "w") as file:
        json.dump(obj, file)
