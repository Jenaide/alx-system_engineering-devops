#!/usr/bin/python3
"""
Created by Jenaide Sibolie
"""
from requests import get
from json import loads


def top_ten(subreddit):
    """
    A function that queries the Reddit API and prints the titles of the first 10 hot
    posts for a given subreddit.
    if not valid subreddit, print None
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    # Set a custom User-Agent header
    headers = {'User-Agent': 'Windows; 11 Home Single Language; 22621.1778; Chrome/113.0.5672.129'}
    response = get(url, headers=headers, allow_redirects=False)
    reddits = response.json()
    try:
        child = reddits.get('data').get('children')
        for i in range(10):
            print(child[i].get('data').get('title'))
    except:
        print('None')
