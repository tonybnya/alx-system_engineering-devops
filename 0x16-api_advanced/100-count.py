#!/usr/bin/python3
"""
# 100-count.py
# Author: @tonybnya

Python script has a recursive function that queries Reddit API, parses the
title of all hot articles, prints a sorted count of given keywords.
"""
import requests


def count_words(subreddit, word_list, after='', count=0, words_count={}):
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
        params=params,
        allow_redirects=False
    )

    try:
        data = res.json()
        if res.status_code == 404:
            raise Exception
    except Exception:
        print('')
        return

    data = res.get('data')
    after = data.get('after')
    count += data.get('dist')

    for child in data.get('children'):
        title = child.get('data').get('title').lower().split()
        for word in word_list:
            if word.lower() in title:
                ntimes = len([t for t in title if t == word.lower()])
                if words_count.get(word) is None:
                    words_count[word] = ntimes
                else:
                    words_count[word] += ntimes

    if after is None:
        if len(words_count) == 0:
            print('')
            return
        words_count = sorted(words_count.items(), key=lambda i: (-i[1], i[0]))
        [print('{}: {}'.format(key, value)) for key, value in words_count]
    else:
        count_words(subreddit, word_list, after, count, words_count)
