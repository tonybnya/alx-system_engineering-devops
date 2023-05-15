#!/usr/bin/python3
"""
# 100-count.py
# Author: @tonybnya

Python script has a recursive function that queries Reddit API, parses the
title of all hot articles, prints a sorted count of given keywords.
"""
import requests


def count_words(subreddit, word_list, after='', words_count={}):
    """
    Main function
    """
    if not words_count:
        for word in word_list:
            if word.lower() not in words_count:
                words_count[word.lower()] = 0

    if after is None:
        words_count = sorted(words_count.items(), key=lambda x: (-x[1], x[0]))
        for word in words_count:
            if word[1]:
                print('{}: {}'.format(word[0], word[1]))
        return None

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {'user-agent': 'tonybnya'}
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
            lower = [word.lower() for word in title.split(' ')]

            for word in words_count.keys():
                words_count[word] += lower.count(word)
    except Exception:
        return None

    count_words(subreddit, word_list, after, words_count)
