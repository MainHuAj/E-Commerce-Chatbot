import streamlit as st
from llm_router import route_query
from faq import ingest_faq_data,faq_chain
from pathlib import Path
from sql import sql_chain
import re

faqs_path = Path(__file__).parent/"resources/faq_data.csv"
ingest_faq_data(faqs_path)

def format_response(text):
    # Convert raw URLs to markdown hyperlinks
    url_pattern = r'(https?://\S+)'
    formatted = re.sub(url_pattern, r'[View Product](\1)', text)
    return formatted

def ask(query):
    route = route_query(query)
    if route == 'faq':
        return faq_chain(query)
    elif route == 'sql':
        response = sql_chain(query)
        return format_response(response)
    else:
        return f"Please ask questions related to women shoes or any general platform related issues like refund policy etc."



st.title("E-Commerce Chatbot")
st.info("ℹ️ This chatbot is specialized for **women's sports shoes** only. Product search outside this category may not return results.")
query = st.chat_input("Write your Query")


if "messages" not in st.session_state:
    st.session_state["messages"] = []
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message["content"])


if query:
    with st.chat_message("user"):
        st.markdown(query)
    st.session_state.messages.append({"role":"user","content":query})
    
    response = ask(query)
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role":"assistant","content":response})


