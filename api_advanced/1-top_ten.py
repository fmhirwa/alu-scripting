#!/usr/bin/python3
"""" Checks to see if the limits is met"""
import requests


def top_ten(subreddit):
    """"Standard API request"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10" \
        .format(subreddit)

    res = requests.get(url,
                       headers={
                           'User-Agent': 'Mozilla/5.0'})

    if res.status_code != 200:
        print(None)
    else:
        json_response = res.json()
        posts = json_response.get('data').get('children')
        [print(post.get('data').get('title')) for post in posts]
