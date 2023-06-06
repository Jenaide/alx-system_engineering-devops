#!/usr/bin/python3
"""
Created by Jenaide Sibolie
"""
from json import loads
from requests import get


def count_words(subreddit, word_list, after=None, word_count=None):
    """
    A Recursive function that queries the reddit api, parses the title of all hot articles
    and prints a sorted count of given keywords.
    """
    if word_count is None:
        word_count = {}
  
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    # Set a custom User-Agent header
    headers = {'User-Agent': 'Windows; 11 Home Single Language; 22621.1778; Chrome/113.0.5672.129'}
    params = {'after': after} if after else None
    response = get(url, headers=headers, params=params, allow_redirects=False)
    reddits = response.json()

    try:
        children = reddits.get('data').get('children')
        for child in children:
            title = child.get('data').get('title')
            for title in children:
                hot_list.append(title)
                for word in word_list:
                    if word.lower() in title.lower().split():
                        if word.lower() in word_count:
                            word_count[word.lower()] += 1
                        else:
                            word_count[word.lower()] = 1

        after = reddits.get('data').get('after')
        if after:
            count_words(subreddit, word_list, after=after)
        else:
            print_word_count(word_count)
    except:
        print(None)

def print_word_count(word_count):
    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0].lower()))
    for word, count in sorted_words:
        print("lowercase word:".format(word.lower(), count))
