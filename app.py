from dotenv import load_dotenv
load_dotenv()
import os
import pickle
import streamlit as st
import pandas as pd
import requests
from sklearn.metrics.pairwise import cosine_similarity

# Load API key from environment
API_KEY = os.getenv("TMDB_API_KEY")

# Load the saved DataFrame and vectorizer
movies_df = pickle.load(open('movies_df.pkl', 'rb'))
cv = pickle.load(open('vectorizer.pkl', 'rb'))

# Calculate vectors on the fly (small memory hit, avoids storing huge file)
vectors = cv.transform(movies_df['tags']).toarray()

st.title('🎬 Movies Recommender System')

# Movie selection dropdown
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movies_df['title'].values
)

# Fetch poster from TMDB API
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    response = requests.get(url)
    data = response.json()

    if 'poster_path' not in data or data.get('status_code') == 34:
        return "https://via.placeholder.com/300x450?text=No+Image"

    poster_path = data['poster_path']
    return f"https://image.tmdb.org/t/p/w500/{poster_path}"

# Recommendation function
def recommend(movie):
    index = movies_df[movies_df['title'] == movie].index[0]
    distances = cosine_similarity([vectors[index]], vectors)[0]
    recommended_indices = distances.argsort()[-6:-1][::-1]  # top 5 excluding itself

    recommended_names = []
    recommended_posters = []
    for i in recommended_indices:
        movie_id = movies_df.iloc[i].id
        recommended_names.append(movies_df.iloc[i].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_names, recommended_posters

# Show recommendations
if st.button('Show Recommendation'):
    names, posters = recommend(selected_movie)
    cols = st.columns(5)
    for col, name, poster in zip(cols, names, posters):
        col.text(name)
        col.image(poster)
