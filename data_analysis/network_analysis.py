import networkx as nx


def create_interaction_network(comments):
    """
    Function to create a network of interactions between users
    """
    G = nx.Graph()
    for comment in comments:
        if 'parent_id' in comment:
            G.add_edge(comment['author'], comment['parent_id'])
    return G