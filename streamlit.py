import streamlit
'Would you like to make a Movie or TV Show?'
movie = st.checkbox('Movie')
show = st.checkbox('Show')

if movie:
    option = st.selectbox(
    'Select the Genre of your Movie',
    ('Comedy', 'Romantic', 'Action'))
if show:
    option = st.selectbox(
    'Select the Genre of your Show',
    ('Comedy', 'Romantic', 'Action'))
