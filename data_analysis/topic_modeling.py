from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation


def extract_topics(comments, num_topics=5, num_words=10):
    """
    Function to extract topics from comments using Latent Dirichlet Allocation
    """
    vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words='english')
    term_matrix = vectorizer.fit_transform(comments)
    lda = LatentDirichletAllocation(n_components=num_topics, random_state=42)
    lda.fit(term_matrix)
    topics = dict()
    for idx, topic in enumerate(lda.components_):
        topics[idx] = [vectorizer.get_feature_names()[i] for i in topic.argsort()[:-num_words - 1:-1]]
    return topics