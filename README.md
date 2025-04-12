# Content-Based Movie Recommendation System

[![GitHub](https://img.shields.io/badge/GitHub-Repo-blue?logo=github)](https://github.com/Kumarpal613/movies_recommender_system)

## Overview

This project implements a content-based movie recommendation system. It leverages movie metadata to provide recommendations to users based on the content of movies they have shown interest in. The system utilizes **TF-IDF (Term Frequency-Inverse Document Frequency)** vectorization to represent movie descriptions and **cosine similarity** to measure the similarity between different movies. An interactive web application is built using **Streamlit** to allow users to easily explore movie recommendations.

## Technologies Used

* **Python:** The primary programming language.
* **Pandas:** For data manipulation and analysis.
* **Scikit-learn (sklearn):** For TF-IDF vectorization and cosine similarity calculation.
* **Streamlit:** For building the interactive web application.

## Data Source

The movie metadata used in this project is the **TMDb Movie Dataset** available on Kaggle:

[TMDb Movie Dataset: Metadata for Film Analysis](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

This dataset provides key information about a large collection of movies sourced from The Movie Database (TMDb) API. It includes details such as movie titles, overviews, release dates, popularity scores, vote averages, and vote counts.

## Data Preprocessing

The movie metadata from the TMDb dataset was processed to clean and prepare it for analysis. This involved steps such as handling missing values and extracting relevant textual information like movie overviews.

## Feature Engineering

The **TF-IDF** technique was applied to the **movie overviews** from the TMDb dataset to convert the textual data into numerical vectors. This allows the system to understand the content of each movie based on the importance of the words within it relative to the entire movie dataset.

## Recommendation Logic

The recommendation system works as follows:

1.  **Data Loading:** The movie metadata is loaded from the TMDb dataset.
2.  **Vectorization:** The 'overview' text for each movie is transformed into a TF-IDF vector.
3.  **Similarity Calculation:** Cosine similarity is calculated between the TF-IDF vectors of all pairs of movies. This metric quantifies the similarity in content between movies.
4.  **Recommendation Generation:** When a user shows interest in a particular movie, the system identifies the movies with the highest cosine similarity scores to that movie and presents them as recommendations.

## Interactive Web Application

A user-friendly web application is built using Streamlit, allowing users to:

* Search for movies from the TMDb dataset.
* Select a movie and get recommendations for similar movies based on their content.
* View the titles and potentially brief descriptions of the recommended movies.

## Setup and Running the Application

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Kumarpal613/movies_recommender_system.git](https://github.com/Kumarpal613/movies_recommender_system.git)
    cd movies_recommender_system
    ```

2.  **Download the Dataset:**
    * Go to the [TMDb Movie Dataset Kaggle page](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).
    * Download the `tmdb_5000_movies.csv` and potentially `tmdb_5000_credits.csv` files (depending on which file you are using for the overviews).
    * Place these CSV files in the appropriate directory within your project (you might need to create a `data` folder).

3.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Ensure your `requirements.txt` file includes:)*
    ```
    pandas
    scikit-learn
    streamlit
    ```

4.  **Run the Streamlit application:**
    ```bash
    streamlit run your_streamlit_app_file.py
    ```
    *(Replace `your_streamlit_app_file.py` with the actual name of your Streamlit application file.)*

## Usage

1.  Open the Streamlit application in your web browser.
2.  Use the search bar to find movies from the TMDb dataset.
3.  Select a movie from the search results to view recommendations for similar movies.

## Future Enhancements (Optional)

* Explore using other features from the TMDb dataset (e.g., genres, keywords) for more comprehensive content-based recommendations.
* Integrate user ratings or feedback (if you plan to incorporate other datasets or functionalities).
* Implement collaborative filtering techniques alongside content-based methods.
* Deploy the application to a cloud platform for broader accessibility.


Remember to replace `your_streamlit_app_file.py` with the actual name of your Streamlit application file. This updated `README.md` provides more specific information about the data source used in your project.
