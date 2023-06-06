#!/usr/bin/python3
"""
Created by Jenaide Sibolie
"""
from json import loads
from requests import get


def recurse(subreddit, hot_list=[]):
    """
    A recursive function that queries the reddit api and returns a list containing
    the title of all hot articles for given subreddit.
    if no results return None.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    # Set a custom User-Agent header
    headers = {'User-Agent': 'Windows; 11 Home Single Language; 22621.1778; Chrome/113.0.5672.129'}
    response = get(url, headers=headers, allow_redirects=False)
    reddits = response.json()

    try:
        children = reddits.get('data').get('children')
        for title in children:
            hot_list.append(title.get('data').get('title'))
        return hot_list
    except:
        print(None)
        return 0
