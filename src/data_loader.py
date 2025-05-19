import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath)
    df['genres'] = df['genres'].fillna('')
    df['description'] = df['description'].fillna('')
    df['combined_features'] = df['genres'] + ' ' + df['description']
    return df
