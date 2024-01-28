#!/usr/bin/python3
"""
recursive function for the reddit api query
returns a list containing the titles of all
hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    """Defines the Reddit API URL for the subreddit's hot posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=25"

    """Adds 'after' parameter if it's provided"""
    if after:
        url += f'&after={after}'

    """Sets a custom User-Agent to avoid Reddit API request issues"""
    headers = {'User-Agent': 'YourBotName/1.0'}

    """Sends a GET request to the API"""
    response = requests.get(url, headers=headers)

    """Checks if the response status code indicates success"""
    if response.status_code == 200:
        try:
            """Parse the JSON response"""
            data = response.json()
            posts = data['data']['children']
            after = data['data']['after']

            if not posts:
                return hot_list
            else:
                for post in posts:
                    hot_list.append(post['data']['title'])

                """Recursively call the function with the 'after' parameter"""
                return recurse(subreddit, hot_list, after)
        except (KeyError, ValueError):
            """Handle JSON parsing errors"""
            return None
    else:
        """Invalid subreddit or another issue with the request"""
        return None
