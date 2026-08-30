import streamlit as st

st.set_page_config(page_title="Hello World", page_icon="👋", layout="centered")

if "show_hello" not in st.session_state:
    st.session_state.show_hello = False

st.title("Hello World")

if st.button("Click me"):
    try:
        st.session_state.show_hello = True
    except Exception as exc:
        st.error(f"Unable to show the greeting: {exc}")

if st.session_state.show_hello:
    st.success("Hello World")
