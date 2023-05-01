#!/usr/bin/python3
"""
This Python script uses a REST API for a given employee ID,
and returns the information about his/her TODO list progress.
"""
import requests
import sys
URL = 'https://jsonplaceholder.typicode.com/'


def main():
	'''Main function.'''
	ID = sys.argv[1]
	users = requests.get("{}users/{}".format(URL, ID)).json()
	todos = requests.get("{}todos/".format(URL), params={'userId': ID}).json()
	tasks = [
		task.get('title') for task in todos if task.get('completed') is True
	]
	done = len(tasks)
	name = users.get('name')
	num = len(todos)

	print("Employee {} is done with tasks({}:{})".format(name, done, num))

	for task in tasks:
		print("\t{}".format(task))


if __name__ == "__main__":
	main()
