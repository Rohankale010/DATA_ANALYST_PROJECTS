<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4d1a0d8 (Update)
# Movie Recommender System

This project is a Movie Recommender System built using Python. The system recommends similar movies based on a selected movie using various features like genres, keywords, cast, and crew.

## Table of Contents
- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Key](#api-key)
- [Conclusion](#conclusion)

## Project Overview 
The Movie Recommender System is designed to suggest movies similar to a user-selected movie. It leverages a combination of movie features including genres, keywords, cast, and crew to generate recommendations. The project uses a dataset from The Movie Database (TMDb) and processes this data to create a content-based recommendation engine using cosine similarity.

The application is built with Python and employs libraries such as Pandas for data manipulation, Scikit-learn for building the recommendation engine, and Streamlit for creating an interactive web interface. By selecting a movie from the dropdown menu, users can receive recommendations of other movies along with their posters, making the experience visually appealing and easy to use.


## Project Structure

```plaintext
<<<<<<< HEAD
<<<<<<< HEAD
Movie Recommender System/
=======
Pizza Sales Analysis/
>>>>>>> 4d1a0d8 (Update)
=======
Movie Recommender System/
>>>>>>> 8b5c008 (Update)
├── data/
│    ├── tmdb_5000_credits.csv
│    └── tmdb_5000_movies.csv
├── notebook/
│    ├── Content_based_recommendation_system.ipynb
│    ├── movies.pkl
│    └── similarity.pkl    
├── script/
│    ├── app.py
│    ├── movies.pkl
│    └── similarity.pkl
├── README.md
└── requirements.txt
```

## Requirements

- Python 3.x
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Pickle
- Streamlit
- Requests

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Rohankale010/DATA_ANALYST_PROJECTS.git
    cd "Movie Recommender System"
    ```

2. Install the required packages:
    ```sh
    pip install pandas numpy scikit-learn nltk pickle-mixin streamlit requests
    or 
    pip install -r requirements.txt
    ```

3. Download the datasets ([tmdb_5000_credits.csv](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata/data) and [tmdb_5000_movies.csv](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata/data)) and place them in the `data/` directory.

4. Ensure you have a valid API key from The Movie Database (TMDb).

## Usage

1. **Data Preprocessing**: Run the Jupyter Notebook to preprocess the data and generate the similarity matrix. This will save the processed data and similarity matrix as pickle files (`movies.pkl` and `similarity.pkl`).

2. **Streamlit Application**: Run the Streamlit app:
    ```sh
    streamlit run script/app.py
    ```

3. **Interact with the Application**: Open the Streamlit interface in your web browser. Select a movie from the dropdown menu and click the "Show Recommendation" button to see the recommended movies along with their posters.

## API Key

Replace the placeholder API key in the `fetch_poster` function within the `script/app.py` file with your actual API key from TMDb:
```python
url = "https://api.themoviedb.org/3/movie/{}?api_key=YOUR_API_KEY&language=en-US".format(movie_id)
```

## Conclusion

The Movie Recommender System is a powerful tool for discovering new movies based on user preferences. By leveraging various movie attributes such as genres, keywords, cast, and crew, the system provides personalized recommendations that enhance the movie-watching experience. The integration of Streamlit allows for an interactive and user-friendly interface, making it easy for users to receive recommendations and explore movie options visually.

<<<<<<< HEAD
=======
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata/data
>>>>>>> b64dd3f (Added Project)
=======
>>>>>>> 4d1a0d8 (Update)
