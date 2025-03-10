#!/usr/bin/python3
"""
Query Reddit API for titles of top ten posts of a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    Return top ten titles for a given subreddit
    Return None if invalid subreddit given
    """
    # Setting a custom user agent
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful
    if response.status_code != 200:
        print(None)
        return

    # Parse the JSON response
    try:
        data = response.json()
    except ValueError:
        print(None)
        return

    # Extract the top ten posts
    top_ten = data.get('data', {}).get('children', [])
    if not top_ten:
        print(None)
        return

    # Print the titles of the top ten posts
    for post in top_ten:
        print(post.get('data', {}).get('title'))

# Example usage:
# top_ten('python')