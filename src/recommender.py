def get_recommendations(title, df, cosine_sim, top_n=5):
    title = title.lower()
    if title not in df['title'].str.lower().values:
        return None  # movie not found

    # Get index of the movie
    idx = df[df['title'].str.lower() == title].index[0]

    # Get pairwise similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort and get top matches
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:top_n + 1]

    # Get recommended movie titles
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices].tolist()
