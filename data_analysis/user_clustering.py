from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer


def cluster_users(comments, num_clusters=5):
    """
    Function to cluster users based on their comments using K-means
    """
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(comments)
    model = KMeans(n_clusters=num_clusters, random_state=42)
    model.fit(X)
    return model.labels_