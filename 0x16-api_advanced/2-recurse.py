#!/usr/bin/python3
"""This module contains a recursive function that queries the Reddit
API and returns a list containing the titles of all hot articles for
a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """ a recursive function that queries the Reddit API and returns
    a list containing the titles of all hot articles for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {
        'limit': 100,
        'count': count
    }
    if after:
        params['after'] = after
    curr_count = count + params['limit']
    headers = {
        'User-Agent': 'UbuntuFocal/1.0'
    }

    response = requests.get(url, params=params, headers=headers,
                            allow_redirects=False)

    if response.status_code == 200:
        response_json = response.json()
        hot_posts = response_json.get('data').get('children')
        for hot_post in hot_posts:
            hot_list.append(hot_post['data']['title'])
    else:
        return None

    after = response_json.get('data').get('after')
    if after is None:
        return hot_list

    return recurse(subreddit, hot_list=hot_list, after=after, count=curr_count)
