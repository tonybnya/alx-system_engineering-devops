#!/usr/bin/python3
"""
# 100-count.py
# Author: @tonybnya

Python script has a recursive function that queries Reddit API, parses the
title of all hot articles, prints a sorted count of given keywords.
"""
import requests


def count_words(subreddit, word_list, after='', words={}):
    """
    Main function
    """
    if not words:
        for word in word_list:
            if word.lower() not in words:
                words[word.lower()] = 0

    if after is None:
        lst = sorted(words.items(), key=lambda x: (-x[1], x[0]))
        for word in lst:
            if word[1]:
                print('{}: {}'.format(word[0], word[1]))
        return None

    url = 'https://reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'tonybnya'}
    params = {'limit': 100, 'after': after}
    res = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if res.status_code != 200:
        return None

    try:
        children = res.json()['data']['children']
        after = res.json()['data']['after']
        for child in children:
            title = child['data']['title']
            low = [word.lower() for word in title.split(' ')]

            for word in words.keys():
                words[word] += low.count(word)

    except Exception:
        return None

    count_words(subreddit, word_list, after, words)
