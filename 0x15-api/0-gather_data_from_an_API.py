#!/usr/bin/python3
"""
This Python script uses a REST API for a given employee id_,
and returns the information about his/her TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
	URL = 'https://jsonplaceholder.typicode.com/'
	users_url = URL + 'users'
	todos_url = URL + 'todos'
	id_ = sys.argv[1]

	users = requests.get(users_url + "/{}".format(users_url)).json()
	todos = requests.get(todos_url, params={"userId": id_}).json()

	completed_tasks = [
		task.get('title') for task in todos if task.get('completed') is True
	]

	done = len(completed_tasks)
	name = users.get('name')
	num = len(todos)

	print("Employee {} is done with tasks({}:{})".format(name, done, num))

	for task in tasks:
		print("\t{}".format(task))
