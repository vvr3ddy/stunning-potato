import requests


def get_bearer_token(client_id, client_secret, user_agent):
    """
    Function to get the bearer token for Reddit API
    """
    auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
    data = {'grant_type': 'password', 'username': 'YOUR_USERNAME', 'password': 'YOUR_PASSWORD'}
    headers = {'User-Agent': user_agent}
    response = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)
    if response.status_code != 200:
        raise Exception(f'Failed to get bearer token: {response.content}')
    TOKEN = response.json()['access_token']
    return TOKEN


def get_comments(subreddit_name, limit=100, client_id=None, client_secret=None, user_agent=None):
    """
    Function to get comments from a subreddit
    """
    TOKEN = get_bearer_token(client_id, client_secret, user_agent)
    headers = {"Authorization": f"bearer {TOKEN}", "User-Agent": user_agent}
    response = requests.get(f"https://oauth.reddit.com/r/{subreddit_name}/hot", headers=headers, params={'limit': limit})
    if response.status_code != 200:
        raise Exception(f'Failed to get comments: {response.content}')
    posts = response.json()['data']['children']
    comments = []
    for post in posts:
        comments.extend(post['data']['selftext'])
    return comments