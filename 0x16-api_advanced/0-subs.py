#!/usr/bin/python3
"""return the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and
    returns the number of subscribers
    """
    URL = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    try:
        result = requests.get(URL)
        if result.status_code != 200:
            raise Exception
        else:
            result = result.json()
    except Exception:
        return 0

    return result['data']['subscribers']
