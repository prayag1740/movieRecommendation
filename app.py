import streamlit as st
import pandas as pd
import pickle, requests

st.title('Movie Recommender System')
pickle_data = pickle.load(open('movie_dict.pkl', 'rb'))
movies_df = pd.DataFrame(pickle_data)
similarity = pickle.load(open('similarity.pkl', 'rb'))


def poster(movie_id):
    
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"

    headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiMDRmYmZmNWFjY2YyYzg1ZGQwNDBjOTdmM2UwNGNhMiIsIm5iZiI6MTcyNTY0NzU3OS45MDQzNDQsInN1YiI6IjY2ZGI0OTc2NWZiZmQ5YzQ4ODc4MzUzMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.0ipllUPwDzh6pFljk1eh6JpDxaThG9A5bTESO5MUQic"
    }

    response = requests.get(url, headers=headers)
    if not response.status_code == 200:
        return None
    response_json = response.json()
    print(movie_id)
    print(response_json, response_json["poster_path"])
    return "https://image.tmdb.org/t/p/w500" + response_json['poster_path']
    


def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
    res = []
    for movie in movies_list:
        data = {"movie_name" : movies_df.iloc[movie[0]].title, "poster" : poster(movies_df.iloc[movie[0]].id)}
        res.append(data)
    return res

movie_selected = st.selectbox('Choose Movie', movies_df['title'].values)

if st.button('Recommend'):
    movie_list = recommend(movie_selected)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.text(movie_list[0]["movie_name"])
        st.image(movie_list[0]["poster"])
    with col2:
        st.text(movie_list[1]["movie_name"])
        st.image(movie_list[1]["poster"])
    with col3:
        st.text(movie_list[2]["movie_name"])
        st.image(movie_list[2]["poster"])
    with col4:
        st.text(movie_list[3]["movie_name"])
        st.image(movie_list[3]["poster"])
    with col5:
        st.text(movie_list[4]["movie_name"])
        st.image(movie_list[4]["poster"])
    
    
        
        
