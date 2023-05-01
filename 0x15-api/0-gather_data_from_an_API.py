#!/usr/bin/python3
"""
This Python script uses a REST API for a given employee ID,
and returns the information about his/her TODO list progress.
"""
import sys
import requests
URL = 'https://jsonplaceholder.typicode.com/'


def main():
    '''Main function.'''
    ID = sys.argv[1]
    # users = requests.get(f"{URL}users/{ID}").json()
    # todos = requests.get(f"{URL}todos/", params={'userId': ID}).json()
    users = requests.get("{}users/{}".format(URL, ID)).json()
    todos = requests.get("{}todos/".format(URL), params={'userId': ID}).json()
    tasks = [
        task.get('title') for task in todos if task.get('completed') is True
    ]
    done = len(tasks)
    num = len(todos)

    # print(f"Employee {users.get('name')} is done withs tasks({done}:{num})")
    print("Employee {} is done withs tasks({}:{})".format(
        users.get('name'), done, num)
    )

    for task in tasks:
        print(f"\t{task}")


if __name__ == '__main__':
    main()
