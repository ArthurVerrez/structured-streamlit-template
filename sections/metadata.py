import streamlit as st
from config import DEFAULT_SESSION_STATE, PAGE_TITLE, PAGE_ICON


def metadata():
    """Sets page config, loads CSS, and initializes session state."""
    st.set_page_config(
        page_title=PAGE_TITLE,
        page_icon=PAGE_ICON,
        initial_sidebar_state="expanded",
    )
    try:
        with open("./static/style.css") as f:
            css = f.read()
            st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("CSS file not found at ./static/style.css")
