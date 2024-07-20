import streamlit as st
import pickle

netflix = pickle.load(open('Deployed Model/netflix.pkl', 'rb'))
similarity = pickle.load(open('Deployed Model/similarity.pkl', 'rb'))
shows = netflix['title'].values
st.title('Netflix Show Recommender by Lucky')
selected_show = st.selectbox('Please Select Show for which you want recommendations', shows)


def recommend(movie):
    movie_index = netflix[netflix['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_shows = []
    for i in movie_list:
        recommended_shows.append(netflix.iloc[i[0]].title)
    return recommended_shows


if st.button('Recommend'):
    recommendations = recommend(selected_show)
    for i in recommendations:
        st.write(i)
