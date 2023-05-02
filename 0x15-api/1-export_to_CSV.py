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
    todos_url = URL + 'todos'

    user = requests.get(users_url).json()
    username = user.get('username')
    todos = requests.get(todos_url, params={"userId": id_}).json()

    with open("{}.csv".format(id_), "w", newline="") as file_obj:
        writer = csv.writer(file_obj, quoting=csv.QUOTE_ALL)

        for todo in todos:
            writer.writerow([id_, todo.get("completed"), todo.get("title")])
