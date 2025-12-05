import streamlit as st

if "count" not in st.session_state:
    st.session_state.count = 0

st.subheader("Counter Example")

def increment():
    st.session_state.count += 1

def reset():
    st.session_state.count = 0

st.write("**Current Count:**", st.session_state.count)

st.button("Increment", on_click=increment)
st.button("Reset", on_click=reset)
