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

##Pyplot chart
import matplotlib.pyplot as plt

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)

##Altair chart
df = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.altair_chart(c, use_container_width=True)

##Vega line chart
df = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])

st.vega_lite_chart(df, {
     'mark': {'type': 'circle', 'tooltip': True},
     'encoding': {
         'x': {'field': 'a', 'type': 'quantitative'},
         'y': {'field': 'b', 'type': 'quantitative'},
         'size': {'field': 'c', 'type': 'quantitative'},
         'color': {'field': 'c', 'type': 'quantitative'},
     },
 })
