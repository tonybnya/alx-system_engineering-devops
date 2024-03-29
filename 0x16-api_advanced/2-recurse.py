#!/usr/bin/python3
"""
# 2-recurse.py
# Author: @tonybnya

Python script has a recursive function that queries Reddit API and returns
a list containing the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, after='', count=0, hot_list=[]):
    """
    Main function
    """
    url = 'https://reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {'User-Agent': 'tonybnya'}
    params = {
        'after': after,
        'count': count,
        'limit': 100
    }
    res = requests.get(
        url,
        headers=headers,
        params=params
    )

    if res.status_code == 404:
        return None

    data = res.json().get('data')
    after = data.get('after')
    count += data.get('dist')

    for child in data.get('children'):
        hot_list.append(child.get('data').get('title'))

    if after is not None:
        return recurse(subreddit, after, count, hot_list)

    return hot_list
