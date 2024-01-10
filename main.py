import os
import time
import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

load_dotenv()
openai_api_key = os.environ['OPENAI_API_KEY']


########################################################################################################################
llm = ChatOpenAI(temperature = 0,
                 model = "gpt-3.5-turbo",
                 streaming = True)

memory = ConversationBufferMemory()

conversation = ConversationChain(
        llm = llm,
        memory = memory,
        verbose = True)

########################################################################################################################
st.set_page_config(page_title = "GPT Langchain")

st.title("GPT Chatbot Using Langchain 🦜👇🏻")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

time.sleep(1)
st.chat_message("assistant").markdown("How can I assist you today")

if prompt := st.chat_input("Enter your message here"):

    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = conversation.predict(input = prompt)

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
