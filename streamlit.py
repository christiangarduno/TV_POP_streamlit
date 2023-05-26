import streamlit as st
'Would you like to make a Movie or TV Show?'
movie = st.checkbox('Movie')
show = st.checkbox('Show')

if movie:
    option = st.selectbox(
    'Select the Genre of your Movie',
    ('Comedy', 'Romantic', 'Action'))
    'Would you like to assign a director or give an average score?'
    director = st.checkbox('Director')
    if director:
        option = st.selectbox(
        'Select a Director',
        ('James Cameron','Wes Anderson','Christopher Nolan'))
    else: 
        score  = st.slider(
    "Average Score of the Director?", 0, 100, 50)
if show:
    option = st.selectbox(
    'Select the Genre of your Show',
    ('Comedy', 'Romantic', 'Action'))
