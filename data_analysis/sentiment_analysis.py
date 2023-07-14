from textblob import TextBlob


def analyze_sentiment(comment):
    """
    Function to analyze the sentiment of a comment using TextBlob
    """
    blob = TextBlob(comment)
    return blob.sentiment.polarity