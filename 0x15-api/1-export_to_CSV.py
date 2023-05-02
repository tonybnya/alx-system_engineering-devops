#!/usr/bin/python3
# Author: @tonybnya
"""
This Python script uses 0-gather_data_from_an_API.py file,
and export data in the CSV format.
"""
import csv
import requests
import sys


if __name__ == "__main__":
    URL = 'https://jsonplaceholder.typicode.com/'
    id_ = sys.argv[1]
    users_url = URL + 'users/' + id_
    tasks_url = URL + 'todos'

    user = requests.get(users_url).json()
    name = user.get('username')
    tasks = requests.get(tasks_url, params={"userId": id_}).json()

    with open("{}.csv".format(id_), "w") as obj:
        for task in tasks:
            status = task.get("completed")
            title = task.get("title")
            obj.write('"{}","{}","{}","{}"'.format(id_, name, status, title))
