import streamlit as st
from config import CURRENT_VERSION, APP_NAME


def header():
    """Displays the application header."""
    st.markdown(
        f"<h1>{APP_NAME}<small>{CURRENT_VERSION}</small></h1>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """Welcome! 👋 This is a template application to demonstrate a structured approach to building Streamlit apps. Feel free to explore the different sections and adapt the code to your needs."""
    )

    st.divider()
