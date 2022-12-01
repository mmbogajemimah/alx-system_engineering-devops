#!/usr/bin/python3
'''
A function that queries the Reddit API and returns
the number of subscribers(Total subscribers)
for a given subreddit. If invalid subreddit
is given, the function should return 0
'''
import requests


def number_of_subscribers(subreddit):
    '''A function that returns the number of subscribers'''
    url = 'https://www.reddit.com/r/{}/top.json'.format(subreddit)
    h = {'User-Agent': 'Chrome/107.0.5304.110'}
    p = {'show': 'all'}
    res = requests.get(url, params=p, headers=h, allow_redirects=False)
    if res.status_code == 200:
        json_output = res.json()
        output = json_output['data']['children'][0]
        return output['data']['subreddit_subscribers']
    else:
        return 0
