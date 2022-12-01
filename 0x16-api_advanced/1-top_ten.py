#!/usr/bin/python3
'''script to get subreddit top ten hot posts'''
import requests


def top_ten(subreddit):
    '''Get number of subscribers for a subreddit
    Arguments:
        subreddit (str): subreddit name
    Returns:
        number of subscribers
    '''

    # Get data
    response = requests.request(
        'GET',
        'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit),
        headers={
            'User-Agent': 'my browser'
        },
        allow_redirects=False
    )

    # Check if successful
    if response.status_code == 200:
        # Get json data
        try:
            hot_posts = response.json().get('data').get('children')

            [print(post.get('data').get('title')) for post in hot_posts]
        except:
            pass
    else:
        print(None)
