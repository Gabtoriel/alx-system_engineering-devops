#!/usr/bin/python3
"""
function that queries the reddit api and
returns the number of subscribers (not active
users, total subscribers) for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """Defines the Reddit API URL for the subreddit's about page"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    """Sets a custom User-Agent to avoid Reddit API request issues"""
    headers = {'User-Agent': 'YourBotName/1.0'}

    """Sends a GET request to the API"""
    response = requests.get(url, headers=headers)

    """Checks if the response status code indicates success"""
    if response.status_code == 200:
        try:
            """Parses the JSON response"""
            data = response.json()
            """Extracts the number of subscribers"""
            subscribers = data['data']['subscribers']
            return subscribers
        except (KeyError, ValueError):
            """Handles JSON parsing errors"""
            return 0
    else:
        """Invalid subreddit or another issue with the request"""
        return 0
