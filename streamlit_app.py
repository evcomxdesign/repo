pip install streamlit-aggrid
from st_aggrid import AgGrid
AgGrid(my_dataframe)

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

st.title('Uber pickups in NYC')

import time

my_bar = st.progress(0)

