#!/usr/bin/python3
"""return the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and
    returns the number of subscribers
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    URL = f'https://www.reddit.com/r/{subreddit}/about.json'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                        AppleWebKit/537.36 (KHTML, like Gecko)\
                        Chrome/91.0.4472.124 Safari/537.36"}

    try:
        result = requests.get(URL, headers=headers)
        result = result.json()
        return result['data']['subscribers']
    except Exception:
        return 0
