import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_lst = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommend_movies = []
    for i in movies_lst:
        recommend_movies.append(movies_list.iloc[i[0]].title)
    return recommend_movies

# Load data
movies_list = pickle.load(open(r'D:\ML\project\movies_recommender_system\movies.pkl', 'rb'))
similarity = pickle.load(open(r'D:\ML\project\movies_recommender_system\similarity.pkl', 'rb'))
movies_list_show = movies_list['title'].values

# Streamlit UI
st.title("\U0001F3A5 Movie Recommender System")

selected_movie_name = st.selectbox(
    "How would you like the movie recommendation?",
    movies_list_show
)

if st.button("\U0001F4AC Recommend"):
    recommendations = recommend(selected_movie_name)
    st.subheader("\U0001F4FA Recommended Movies")
    for idx, movie in enumerate(recommendations, start=1):
        st.write(f"{idx}. {movie}")