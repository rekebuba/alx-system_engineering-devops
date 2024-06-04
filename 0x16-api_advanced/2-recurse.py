#!/usr/bin/python3
"""advanced API"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Write a recursive function that queries the Reddit API
    and returns a list containing the titles of all hot articles
    for a given subreddit.
    """
    URL = f'https://www.reddit.com/r/{subreddit}/hot/.json?after={after}'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                        AppleWebKit/537.36 (KHTML, like Gecko)\
                        Chrome/91.0.4472.124 Safari/537.36"}

    try:
        result = requests.get(URL, headers=headers)
        if result.status_code != 200:
            raise Exception
        else:
            result = result.json()
            for i, data in enumerate(result['data']['children']):
                hot_list.append(data['data']['title'])
    except Exception:
        return None

    if result['data']['after']:
        recurse(subreddit, hot_list=hot_list, after=result['data']['after'])

    return hot_list
