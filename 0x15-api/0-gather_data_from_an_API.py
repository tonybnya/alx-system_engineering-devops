#!/usr/bin/python3
"""
This Python script uses a REST API for a given employee id_,
and returns the information about his/her TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    URL = 'https://jsonplaceholder.typicode.com/'
    id_ = sys.argv[1]
    users_url = URL + 'users/' + id_
    todos_url = URL + 'todos'

    user = requests.get(users_url).json()
    todos = requests.get(todos_url, params={"userId": id_}).json()

    dones = [i.get('title') for i in todos if i.get('completed') is True]

    done = len(dones)
    name = user.get('name')
    tasks = len(todos)

    print("Employee {} is done with tasks({}/{}):".format(name, done, tasks))
    for task in dones:
        print("\t {}".format(task))
