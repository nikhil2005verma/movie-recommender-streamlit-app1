import streamlit as st
import pickle
import numpy as np
import pandas as pd
import requests


def fetch_poster(movie_id):
    # url = "https://api.themoviedb.org/3/movie/{movie_id}?api_key=2d54003ca5b89f699e5234e5e086c5eb&language=en-US".format(movie_id)
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=2d54003ca5b89f699e5234e5e086c5eb&language=en-US".format(movie_id))
    data = response.json()
    st.writ
    poster_path = data['poster_path']
    return ("https://image.tmdb.org/t/p/w500/" + poster_path)



def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movie_poster=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movie_poster.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movie_poster


movies_dict=pickle.load(open("movies_dict.pkl", "rb"))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open("similarity.pkl", "rb"))

st.title("Movie recommend System")
selected_movie_name = st.selectbox('how would you like to be contacted',movies['title'].values)

if st.button('recommend'):
    name,posters=recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(name[0])
        st.image(posters[0])
    with col2:
        st.text(name[1])
        st.image(posters[1])

    with col3:
        st.text(name[2])
        st.image(posters[2])
    with col4:
        st.text(name[3])
        st.image(posters[3])
    with col5:
        st.text(name[4])
        st.image(posters[4])










