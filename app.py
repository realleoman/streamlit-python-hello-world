from contextlib import nullcontext

import streamlit as st

st.set_page_config(page_title="Hello World", page_icon="👋", layout="centered")

st.markdown(
    """
    <style>
        .stApp {
            background:
                linear-gradient(rgba(0, 0, 0, 0.45), rgba(0, 0, 0, 0.55)),
                repeating-linear-gradient(
                    0deg,
                    rgba(28, 255, 156, 0.12) 0px,
                    rgba(28, 255, 156, 0.12) 1px,
                    transparent 1px,
                    transparent 4px
                ),
                #03130f;
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }

        .hello-card,
        div[data-testid="stVerticalBlock"] {
            background: rgba(3, 17, 13, 0.72);
            border: 1px solid rgba(124, 255, 196, 0.35);
            border-radius: 16px;
            padding: 2rem;
            box-shadow: 0 0 20px rgba(28, 255, 156, 0.2);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

card_container = st.container() if hasattr(st, "container") else nullcontext()

# Apply the visual card styling to the actual Streamlit container instead of a
# standalone raw HTML block that does not wrap subsequent widgets.
with card_container:
    st.title("Hello World")

    if st.button("Click me"):
        st.success("Hello World")
