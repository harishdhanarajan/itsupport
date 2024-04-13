import os
from abc import ABC, abstractmethod
from typing import Tuple
import streamlit as st

class AbstractPage(ABC):
	@abstractmethod
	def display_page(self):
		pass
		
	@abstractmethod
	def _display_content(self):
		pass

class AbstractContentPage(AbstractPage, ABC):
    _content_placeholder: st.container
    
    def display_page(self):
        self.__display_logo()
        self._content_placeholder.empty()
        with self._content_placeholder.container():
            self._display_content()