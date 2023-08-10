#!/usr/bin/python3
"""
# 0-subs.py
# Author: @tonybnya

Python script queries the Reddit API and returns the number of subscribers.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Main function
    """
    url = 'https://reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'tonybnya'}
    res = requests.get(url, headers=headers)
    subscribers = res.json().get('data', {}).get('subscribers', 0)

    return subscribers
