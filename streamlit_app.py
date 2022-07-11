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

