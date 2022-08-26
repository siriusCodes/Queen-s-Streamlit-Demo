import streamlit as st
import pandas as pd

st.title("Demo Dashboard")
st.write("Example dashboard in Marquee Class")

categories = ['A','B','C']
st.multiselect('pick an option', categories)

st.sidebar.button('Click me!')

url = "https://www.iposcoop.com/last-100-ipos/"
dfs = pd.read_html(url)
df = dfs[0]


