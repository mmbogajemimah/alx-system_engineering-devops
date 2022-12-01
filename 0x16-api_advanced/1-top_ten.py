#!/usr/bin/python3
# A function that queries the Reddit API and
# prints the titles of the first
# 10 hot posts listed for a given subreddit
# If not a valid subreddit, print None.

import requests


def top_ten(subreddit):
    '''A function that returns and prints
    the titles of the first 10 hot posts'''
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    h = {'User-Agent': 'Chrome/107.0.5304.110'}
    p = {'limit': 10}
    res = requests.get(url, params=p, headers=h, allow_redirects=False)

    if res.status_code == 200:
        for post in res.json()['data']['children']:
            print(post['data']['title'])

    else:
        print(None)
