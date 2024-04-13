import os
import pandas as pd
import streamlit as st
from pages_views.abstract_page import AbstractContentPage

class ITSupport():
    def __init__(self,page_id: int):
        super().__init__()
        if page_id == 2:
            self._content_placeholder = st.container()
        else:
            self._content_placeholder = st.empty()
    def display_page(self):
        st.markdown("<p style = 'text-align:center;'> Please use the below search bar for your issues - Presented by BNYM. </p>", unsafe_allow_html = True)
        user_query = st.text_input("", value = "")
        links = pd.read_excel("links.xlsx")
        model = SentenceTransformer('bert-base-nli-mean-tokens')
        embeddings = model.encode(links['Description'].tolist())
        query_embedding = model.encode([user_query])[0]
        similarities = cosine_similarity([query_embedding], embeddings)[0]
        indices = similarities.argsort()[-top_n:][::-1]
        relevant_results = []
        
        for idx in indices:
            if any(keyword.lower() in links.iloc[idx]['Description'].lower() for keyword in user_query.split()):
                relevant_results.append(links.iloc[idx])
                
        results = pd.DataFrame(relevant_results)
        
        if results.empty:
            print('No Relevant Topics to Display')
        else:
            N_cards_per_row = 2
                
            if user_query:
                for n_row, row in results.reset_index().iterrows():
                    i = n_row%N_cards_per_row
                    if i==0:
                        st.write("---")
                        cols= st.columns(N_cards_per_row, gap = "large")
                        
                    with cols[n_row%N_cards_per_row]:
                        st.markdown("---")
                        st.markdown(f"**{row['Description'].strip()}**")
                        st.markdown(f"**{row['Related To'].strip()}**")
                        st.markdown(f"**{row['Link']}**")
                            