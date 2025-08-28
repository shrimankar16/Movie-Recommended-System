import streamlit as st
import pickle
import pandas as pd

# Load data
movies_dict = pickle.load(open('movie_list.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie_title):
    # Get the index of the selected movie
    movie_index = movies[movies['title'] == movie_title].index[0]
    
    # Fetch similarity scores for that movie
    distances = similarity[movie_index]
    
    # Sort movies based on similarity
    movie_indices = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:11]
    
    recommended_movies = []
    for i in movie_indices:
        recommended_movies.append(movies.iloc[i[0]].title)
        
    return recommended_movies

# Streamlit UI
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie:',
    movies['title'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
