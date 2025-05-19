from data_loader import load_data
from feature_extraction import create_tfidf_matrix, compute_similarity
from recommender import get_recommendations

def main():
    print("🎬 Movie Recommendation System 🎬")
    print("---------------------------------")

    # Load and process data
    df = load_data('../data/dataset_movie.csv')
    tfidf_matrix = create_tfidf_matrix(df)
    cosine_sim = compute_similarity(tfidf_matrix)

    while True:
        title = input("\nEnter a movie name (or type 'exit' to quit): ").strip()
        if title.lower() == 'exit':
            print("Goodbye! 👋")
            break

        recommendations = get_recommendations(title, df, cosine_sim)
        if recommendations:
            print(f"\n💡 Because you liked '{title}', you may also like:")
            for i, movie in enumerate(recommendations, 1):
                print(f"{i}. {movie}")
        else:
            print(f"❌ Sorry, we couldn't find '{title}' in the database.")

if __name__ == "__main__":
    main()
