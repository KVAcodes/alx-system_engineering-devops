#!/usr/bin/python3
"""Contains a function that queries the Reddit API and returns the
number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API and returns the number of subscribers."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'UbuntuFocal/1.0'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        subreddit_json = response.json()
        return subreddit_json['data']['subscribers']
    return 0
