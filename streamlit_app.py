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
