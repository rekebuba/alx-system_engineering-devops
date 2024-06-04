#!/usr/bin/python3
"""Advance API"""

import requests


def count_words(subreddit, word_list, after="", titles=""):
    """parses the title of all hot articles, and prints
    a sorted count of given keywords (case-insensitive, delimited by spaces"""
    URL = f"https://www.reddit.com/r/{subreddit}/hot/.json?after={after}"
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

            for data in result['data']['children']:
                titles = titles + data['data']['title'] + " "

        if result['data']['after']:
            count_words(
                subreddit,
                word_list,
                after=result['data']['after'],
                titles=titles
            )
        else:
            count = {}
            for word in word_list:
                count[word] = 0

            result = [x.lower() for x in titles.split()]
            for word in count.keys():
                if word.lower() in result:
                    count[word] += result.count(word.lower())

            for _ in range(len(count)):
                highst = max(count, key=count.get)
                double_val = sorted(
                    [k for k, v in count.items() if count[highst] == v])
                if (double_val[0].lower() == double_val[1].lower()):
                    count[double_val[0]] += count[double_val[1]]
                    del count[double_val[1]]

                if count[highst] != 0:
                    print(f"{double_val[0].lower()}: {count[highst]}")

                del count[double_val[0]]
    except Exception:
        pass
