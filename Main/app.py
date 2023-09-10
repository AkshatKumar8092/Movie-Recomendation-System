import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = movies_dict = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System\nBy Anonymous-Team')
st.divider()

selected_movie_name = st.selectbox('How Would like to be contacted?', movies['title'].values)

if st.button('Recommend'):
    st.write('Similar Movies For The movie 👉 '+selected_movie_name+':')
    st.divider()
    recommendations = recommend(selected_movie_name)
    j = 1
    for i in recommendations:
        st.write(j,i)
        j+=1

st.divider()
st.markdown(":red[Akshat Kumar] |  **:blue[20ETCS002009]**")
st.markdown(":red[DebadriRaj Das] |  **:blue[20ETCS002042]**")
st.markdown(":red[Dhruthi K. Acharya] |  **:blue[20ETCS002047]**")
st.markdown(":red[Kannan Dharun] |  **:blue[20ETCS002063]**")
st.markdown(":red[Shaan Vazarkar] |  **:blue[20ETCS002301]**")
st.divider()

