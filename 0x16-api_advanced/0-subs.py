#!/usr/bin/python3
"""return the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and
    returns the number of subscribers
    """
    URL = f'https://www.reddit.com/r/{subreddit}/about.json'

    try:
        result = requests.get(URL)
        if result.status_code != 200:
            raise Exception
        else:
            result = result.json()
    except Exception:
        return 0

    return result['data']['subscribers']
