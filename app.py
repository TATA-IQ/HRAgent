import streamlit as st
import time
from Agent.graph import  app
from collections import deque 
import uuid
import os
os.environ["OPENAI_API_KEY"]="None"

from langchain_core.chat_history import InMemoryChatMessageHistory

chats_by_session_id = {}



dq=deque(maxlen=10)
st.set_page_config(  
    page_title="Chat App",  
    layout="wide",  
    initial_sidebar_state="collapsed",  
)  
st.title("HR Bot Agent")
if "messages" not in st.session_state:  
    st.session_state.messages = []  
for msg in st.session_state.messages:  
    with st.chat_message(msg["role"]):  
        st.write(msg["content"])  
prompt = st.chat_input("Say something...")  

if prompt:  
    # Add user message to chat  
    st.session_state.messages.append({"role": "user", "content": prompt})  
    with st.chat_message("user"):  
        st.write(prompt)  

    # Add a simple bot response
    result=app.invoke(
        input={"question": prompt}
    )  
    time.sleep(1)  # A brief pause to make it feel more natural  
    bot_response = result["generation_llama"]  
    # dq.append(bot_response)
    st.session_state.messages.append({"role": "bot", "content": bot_response})  
    with st.chat_message("bot"):  
        st.write(bot_response)  