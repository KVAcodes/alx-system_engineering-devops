#!/usr/bin/python3
"""This module defines a function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {
        'limit': 10
    }
    headers = {
        'User-Agent': 'UbuntuFocal/1.0'
    }
    response = requests.get(url, headers=headers, params=params)
    if (response.status_code == 200):
        hot_posts = response.json().get('data').get('children')
        for hot_post in hot_posts:
            print(hot_post['data']['title'])
    else:
        print(None)
