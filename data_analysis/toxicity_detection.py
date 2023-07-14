import requests


def detect_toxicity(comment, api_key):
    """
    Function to detect toxicity in a comment using the Perspective API
    """
    url = 'https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze'
    data = {
        'comment': {'text': comment},
        'languages': ['en'],
        'requestedAttributes': {'TOXICITY': {}}
    }
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {api_key}'}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code != 200:
        raise Exception(f'Failed to detect toxicity: {response.content}')
    toxicity_score = response.json()['attributeScores']['TOXICITY']['summaryScore']['value']
    return toxicity_score