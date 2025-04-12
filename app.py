import streamlit as st
from sections.metadata import metadata
from sections.header import header
from sections.body import body
from sections.footer import footer
from sections.sidebar import sidebar

metadata()
sidebar()
header()
body()
footer()
