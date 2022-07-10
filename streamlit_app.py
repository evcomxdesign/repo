import streamlit as st
import pandas as pd
import numpy as np

#API reference
##Write and magic
st.write(1234)
st.write(pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40],
 }))

if st.button('Say hello'):
     st.write('Why hello there')
 else:
     st.write('Goodbye')
     
     option = st.selectbox(
     'How would you like to be contacted?',
     ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

genre = st.radio(
     "What's your favorite movie genre",
     ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
     st.write('You selected comedy.')
 else:
     st.write("You didn't select comedy.")
