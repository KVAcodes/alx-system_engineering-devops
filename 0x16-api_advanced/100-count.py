#!/usr/bin/python3\
"""This module contains a recursive function that querries the Reddit API,
parses the title of all hot articles and prints a sorted count of given
keywords provided in a list.
"""
import requests
import re


def count_words(subreddit, word_list, keywords={}, after="", count=0):
    """
    Queries Reddit API

    recursively querries the Reddit API , parses the title of all hot articles,
    and prints a sorted count of given keywords (case-insensitive, delimited by
    spaces. Javascript should count as javascript, but java should not).

    """
    if not keywords:
        keywords = {word: 0 for word in word_list}
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
            title = hot_post['data']['title']
            for key in keywords:
                pattern = r'\b{}\b'.format(re.escape(key))
                no_of_matches = len(re.findall(pattern, title, re.IGNORECASE))
                if no_of_matches:
                    keywords[key] += no_of_matches
    else:
        return None

    after = response_json.get('data').get('after')
    if after is None:
        unique = set([key.lower() for key in keywords.keys()])
        merged_dict = {word: 0 for word in unique}
        for key in keywords.keys():
            merged_dict[key.lower()] += keywords[key]

        sorted_dict = {
            k: v for k, v in sorted(merged_dict.items(),
                                    key=lambda item: (-item[1], item[0]))
        }
        for key, val in sorted_dict.items():
            if val > 0:
                print(key + ':', val)
        return

    return count_words(subreddit, word_list, keywords=keywords,
                   after=after, count=curr_count)
