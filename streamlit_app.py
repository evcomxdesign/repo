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

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

#Charts
##Line chart
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

##Area chart
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.area_chart(chart_data)

##Bar chart
chart_data = pd.DataFrame(
     np.random.randn(50, 3),
     columns=["a", "b", "c"])

st.bar_chart(chart_data)

st.title('This is a title')
st.header('This is a header')
st.subheader('This is a subheader')
st.caption('This is a string that explains something above. This is a string that explains something aboveThis is a string that explains something aboveThis is a string that explains something aboveThis is a string that explains something aboveThis is a string that explains something aboveThis is a string that explains something aboveThis is a string that explains something aboveThis is a string that explains something aboveThis is a string that explains something aboveThis is a string that explains something aboveThis is a string that explains something aboveThis is a string that explains something above')
code = '''def hello():
     print("Hello, Streamlit!")'''
st.code(code, language='python')
st.text('This is some text.')
st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')

st.text('This is some text.')

col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")
     
import streamlit as st

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

import time

my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.1)
     my_bar.progress(percent_complete + 1)
     
     with st.spinner('Wait for it...'):
    time.sleep(5)
st.success('Done!')
