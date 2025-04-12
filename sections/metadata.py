import streamlit as st
from config import DEFAULT_SESSION_STATE, PAGE_TITLE, PAGE_ICON


def metadata():
    st.set_page_config(
        page_title=PAGE_TITLE,
        page_icon=PAGE_ICON,
        initial_sidebar_state="expanded",
    )
    with open("./static/style.css") as f:
        css = f.read()
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

    st.session_state.update(DEFAULT_SESSION_STATE)
