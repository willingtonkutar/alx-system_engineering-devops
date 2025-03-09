"""
Function to print hot posts on a given Reddit subreddit.
"""
import requests

def top_ten(subreddit):
    """
    Print the titles of the 10 hottest posts on a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code != 200:
        print("None")
        return
    results = response.json().get("data")
    if results is None:
        print("None")
        return
    for post in results.get("children", []):
        print(post.get("data", {}).get("title"))

# Example usage:
# top_ten('python')