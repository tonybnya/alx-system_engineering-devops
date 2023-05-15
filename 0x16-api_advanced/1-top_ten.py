#!/usr/bin/python3
"""
# 1-top_ten.py
# Author: @tonybnya

Python script queries the Reddit API and prints the titles of the first 10
host posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Main function
    """
    url = 'https://reddit.com/r/{}/hot/.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'tonybnya'}
    res = requests.get(url, headers=headers)
    children = res.json().get('data').get('children')
    # posts = res.json()

    for child in children:
        print(child.get('data').get('title'))
