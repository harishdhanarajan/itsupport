import logging
import streamlit as st

def __init_page_id():
	if "__page_id" not in st.session_state:
		logging.info("No state for 'page_id' found, initializing with '1'.")
		st.session_state.__page_id = 1

def set_page_id(page_id: int):
	__init_page_id()
	st.session_state.__page_id = int(page_id)

def get_page_id():
	__init_page_id()
	return st.session_state.__page_id