# !pip install streamlit
# !python -m streamlit run main.py

import streamlit as st

# Sidebar
st.sidebar.title("Sidebar")
st.sidebar.write("We are on Sidebar now!")
st.sidebar.button("We are on Sidebar now!")

# Columns
col1, col2, col3 = st.columns([1, 2, 1])  # col1 is twice as wide as col2
with col1:
    st.write("This is the first column")
    st.write("This is the first column")
    st.write("This is the first column")
    st.write("This is the first column")
    st.write("This is the first column")
    st.button("Click me in col1")
with col2:
    st.write("This is the second column")
    st.button("Click me in col2")
with col3:
    st.write("This is the first column")
    st.write("This is the first column")
    st.write("This is the third column")
    st.button("Click me in col3")

# Tabs
tab1, tab2, tab3 = st.tabs(["Chart", "Data", "Info"])
with tab1:
    st.write("Chart view")
with tab2:
    st.write("Data view")
with tab3:
    st.write("Information view")

# Container
cont= st.container()
st.write("This is inside the container")
cont.line_chart([1, 2, 3])
st.write("This is outside the container")

with st.container():
    st.write("This content is grouped")
    st.button("Grouped Button")
