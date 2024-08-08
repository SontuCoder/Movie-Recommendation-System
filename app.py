import streamlit as st
import pickle
import pandas as pd
import requests


def poster(a):
    response = 'https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(a)
    data = requests.get(response)
    data1 = data.json()
    return 'https://image.tmdb.org/t/p/w500' + data1['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]

    movie_list = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies = []
    recommend_movies_poster = []
    for i in movie_list:
        # fetch posters from API:
        recommend_movies_poster.append(poster(movies.iloc[i[0]].movie_id))

        recommend_movies.append(movies.iloc[i[0]].title)

    return recommend_movies, recommend_movies_poster


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movies Recommender System:-')

selected_movie = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values
)

if st.button('Recommend'):
    recommendations, posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommendations[0])
        st.image(posters[0])
    with col2:
        st.text(recommendations[1])
        st.image(posters[1])
    with col3:
        st.text(recommendations[2])
        st.image(posters[2])
    with col4:
        st.text(recommendations[3])
        st.image(posters[3])
    with col5:
        st.text(recommendations[4])
        st.image(posters[4])
