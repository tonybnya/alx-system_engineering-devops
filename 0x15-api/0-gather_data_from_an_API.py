#!/usr/bin/python3
"""This Python script uses a REST API for a given employee ID,
and returns the information about his/her TODO list progress.
"""
import requests
import sys
URL = 'https://jsonplaceholder.typicode.com/'


def main(ID):
    '''Main function.'''
    users = requests.get(f"{URL}users/{ID}").json()
    todos = requests.get(f"{URL}todos/", params={'userId': ID}).json()
    tasks = [
        task.get('title') for task in todos if task.get('completed') is True
    ]
    done = len(tasks)
    num = len(todos)

    print(f"Employee {users.get('name')} is done withs tasks({done}:{num})")

    for task in tasks:
        print(f"\t{task}")


if __name__ == '__main__':
    ID = sys.argv[1]
    main(ID)
