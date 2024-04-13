import os
import streamlit as st

from page_views.abstract_page import AbstractContentPage

class HowToPage():
    def __init__(self,page_id: int):
        super().__init__()
        if page_id == 1:
            self._content_placeholder = st.container()
        else:
            self._content_placeholder = st.empty()
    def display_page(self):
        st.write("In General, Content Content")
        st.header("How to Use this Page")
        st.write("Content Content")
        st.subheader("Sub Content")
        st.write("Content Content")
        with st.expander(label = "How to Video", expanded = False):
            st.write("It is expanding")
