import streamlit as st
from config import QUICK_LINKS


def sidebar():
    """Displays the sidebar with quick links."""
    st.sidebar.container(height=30, border=False)

    st.sidebar.subheader("Quick Links")

    for link_data in QUICK_LINKS:
        with st.sidebar.container(border=True):
            col1, col2 = st.columns([1, 6])
            col1.markdown(
                f'<image src="app/{link_data["image"]}" width="25" style="display: block; margin-left: auto; margin-right: auto; background:white; border-radius: 25%;">',
                unsafe_allow_html=True,
            )
            col2.markdown(f"[{link_data['text']}]({link_data['link']})")
