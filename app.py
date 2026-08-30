import streamlit as st

st.set_page_config(page_title="Hello World", page_icon="👋", layout="centered")

if "show_hello" not in st.session_state:
    st.session_state.show_hello = False

st.title("Hello World")

if st.button("Click me"):
    st.session_state.show_hello = True
