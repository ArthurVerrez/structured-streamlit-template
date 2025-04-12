import streamlit as st
from config import GITHUB_USERNAME, GITHUB_REPOSITORY_LINK


def footer():
    st.divider()
    st.markdown(
        f""":grey[Made with 🩵 by [{GITHUB_USERNAME}](https://github.com/{GITHUB_USERNAME}). Check out the code on [GitHub]({GITHUB_REPOSITORY_LINK}).]"""
    )
