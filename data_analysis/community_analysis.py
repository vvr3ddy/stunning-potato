def analyze_community(comments):
    """
    Function to analyze a community
    """
    total_comments = len(comments)
    unique_users = len(set(comment['author'] for comment in comments))
    return {'total_comments': total_comments, 'unique_users': unique_users}