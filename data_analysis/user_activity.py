from collections import Counter


def analyze_user_activity(comments):
    """
    Function to analyze user activity in a subreddit
    """
    users = [comment['author'] for comment in comments]
    user_activity = Counter(users)
    return user_activity.most_common()