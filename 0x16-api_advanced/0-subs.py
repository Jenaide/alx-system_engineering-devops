#!/usr/bin/python3
"""
Created by Jenaide Sibolie
"""
from requests import get
from json import loads


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API.
    Return: the number of subscribers(non active users, total subscribers)
    if invalid the function should return 0.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Windows; 11 Home Single Language; 22621.1778; Chrome/113.0.5672.129'}

    response = get(url, headers=headers)
    reddits = response.json()

    try:
        subscribers = reddits.get('data').get('subscribers')
        return int(subscribers)
    except:
        return 0
