import streamlit as st
import state
import hydralit_components as hc
import os
from page_views.howto import HowToPage
from page_views.itsupport import ITSupport

st.set_page_config(
			page_title = "IT Assist",
			layout = "wide",
)

st.markdown("<h1 style='text-align: center; background-color: #E2EAF4; color: #FFFFFF'>Welcome to IT Support</h1>", unsafe_allow_html = True)
st.markdown("<h4 style='text-align: center; background-color: #E2EAF4; color: #FFFFFF'>Access and Technology Hub for BNYM</h4>", unsafe_allow_html = True)

menu_data = [
		{'id': 1, 'label': "How To", 'key' : "md_how_to", 'icon' : "fa fa-home"},
		{'id': 2, 'label': "IT Support", 'key' :"md_it_support"},		
		{'id': 3, 'label': "Feedback Form", 'key' : "md_feedback"}
]

state.set_page_id(int(hc.nav_bar(
	menu_definition = menu_data,
	hide_streamlit_markers = False,
	sticky_nav = True,
	sticky_mode = 'pinned',
	override_theme = {'menu_background':'#4c00a5'}
)))

__howto_page = HowToPage(state.get_page_id())
__it_support_page = ITSupport(state.get_page_id())

if state.get_page_id() == 1:
	__howto_page.display_page()
if state.get_page_id() == 2:
	__it_support_page.display_page()
