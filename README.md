# 🎬 Movie Recommendation System

---
## 📚 Table of Contents:

- [Description](#-description)
- [Screenshot](#-screenshot-)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Example](#example)
- [Features](#-features)
- [Contact](#-contact)
---

## 📄 Description:

A content-based Movie Recommendation System built using Python. It suggests movies similar to the one entered by the user based on genres and descriptions using TF-IDF and cosine similarity.

---
## 📸 Screenshot: 
![Screenshot 2025-05-19 211108.png](../../../../../Pictures/Screenshots/Screenshot%202025-05-19%20211108.png)
---

## 🗂️ Project Structure
```
movie_recommendation_system/
│
├── data/ # Folder for dataset
│ └── dataset_movie.csv               # Movie dataset with id, title, genres, description
│
├── src/ # Source code
│ ├── main.py                  # Entry point for running the app
│ ├── data_loader.py           # Loads and preprocesses movie data
│ ├── feature_extraction.py    # TF-IDF vectorization and similarity calculations
│ └── recommender.py           # Movie recommendation logic
│
├── .venv/ 
│
├── requirements.txt 
└── README.md 
```

---

## ⚙️ Installation

Follow these steps to set up and run the project locally:

1. **Clone the repository:**
   ```bash
      git clone https://github.com/yourusername/movie-recommendation-system.git
      cd movie-recommendation-system
   ```
2. **Install The Requirements**
  ```bash
     pip install -r requirements.txt
  ```
3. **Run The Project**
```bash
   python src/main.py
   ## Ensure data/movies.csv includes headers: movie_id,title,genres,description.
```




--- 

# 🚀 Usage:
- Once the program starts:
- Enter a movie title when prompted.
- Get a list of similar movies recommended.
- Type exit to quit the app.

---

## Example
```
🎬 Movie Recommendation System 🎬
---------------------------------

Enter a movie name (or type 'exit' to quit): The Godfather

💡 Because you liked 'The Godfather', you may also like:
1. The Godfather: Part II
2. The Godfather: Part III
3. Blood Ties
4. Snabba Cash
5. Four Brothers

Enter a movie name (or type 'exit' to quit): 
```

---

# ✨ Features
- Simple command-line interface
- Recommends similar movies using:
- TF-IDF vectorization
- Cosine similarity
- Handles missing data gracefully
- Easy to extend with more features or a GUI

# 🤝 Contributing
## Contributions are welcome! To contribute:

--- 

# 📄 License
This project is licensed under the MIT License.

--- 

# 📬 Contact
GitHub: HariomSinghalPuri

Email: www.singhalpuri.com

---
## ⭐ If you like this project, give it a star!


