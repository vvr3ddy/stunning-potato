import pandas as pd


def analyze_time_series(comments, timestamps):
    """
    Function to analyze comments over time
    """
    df = pd.DataFrame({'comment': comments, 'timestamp': pd.to_datetime(timestamps)})
    df.set_index('timestamp', inplace=True)
    daily_comments = df.resample('D').count()
    return daily_comments