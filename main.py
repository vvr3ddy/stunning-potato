from data_collection.reddit_api import get_comments
from data_analysis.toxicity_detection import detect_toxicity
from data_analysis.sentiment_analysis import analyze_sentiment
from data_analysis.topic_modeling import identify_topics
from data_analysis.user_clustering import cluster_users
from data_analysis.time_series_analysis import analyze_time_series
from data_analysis.network_analysis import create_interaction_network
from data_visualization.visualization import create_bar_chart, create_pie_chart, create_histogram, create_network_diagram

# Define your Reddit API key and the name of the subreddit you want to analyze
reddit_api_key = 'your_reddit_api_key'
subreddit_name = 'subreddit_name'

# Get comments from the subreddit
comments = get_comments(reddit_api_key, subreddit_name)

# Detect toxicity in the comments
toxicity_scores = [detect_toxicity(comment) for comment in comments]

# Analyze sentiment in the comments
sentiment_scores = [analyze_sentiment(comment) for comment in comments]

# Identify topics in the comments
topics = identify_topics(comments)

# Cluster users based on their comments
user_clusters = cluster_users(comments)

# Analyze comments over time
timestamps = [comment['timestamp'] for comment in comments]
daily_comments = analyze_time_series(comments, timestamps)

# Create a network of interactions between users
G = create_interaction_network(comments)

# Visualize the results
create_bar_chart(toxicity_scores, title='Toxicity Scores', xlabel='Score', ylabel='Number of Comments')
create_pie_chart(sentiment_scores, labels=['Negative', 'Neutral', 'Positive'], title='Sentiment Scores')
create_histogram(topics, title='Topics', xlabel='Topic', ylabel='Number of Comments')
create_network_diagram(G)