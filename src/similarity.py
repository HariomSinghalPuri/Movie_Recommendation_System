from sklearn.metrics.pairwise import cosine_similarity

def compute_cosine_similarity(tfidf_matrix):
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return cosine_sim
