#!/usr/bin/python3
"""advanced API"""

import requests


def top_ten(subreddit):
    """
    titles of the first 10 hot posts listed for a given subreddit.
    """
    URL = f'https://www.reddit.com/r/{subreddit}/hot/.json'
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
                if i < 10:
                    print(data['data']['title'])
    except Exception:
        print("None")
