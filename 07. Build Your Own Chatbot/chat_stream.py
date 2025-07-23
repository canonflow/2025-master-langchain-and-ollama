import uuid
import streamlit as st
import os
from streamlit_chat import message
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    ChatPromptTemplate
)
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from utils import (
    get_session_history,
    chat_with_llm
)

st.html(
    """
  <style>
    [class*="st-key-ai"] {
        background-color: #262730;
        color: #fafafa
    }
  </style>
  """
)




def chat_message(name):
    return st.container(key=f"{name}-{uuid.uuid4()}").chat_message(name=name)


# ===== SETUP LLM =====
load_dotenv("./../.env")

BASE_URL = os.getenv("OLLAMA_BASE_URL")
MODEL = "llama3.2:latest"

LLM = ChatOllama(
    base_url=BASE_URL,
    model=MODEL,
)

# ===== SETUP MESSAGES =====
system = SystemMessagePromptTemplate.from_template(
    """
    You are a helpful assistant who embodies the calm, intelligent, and refined demeanor of Jarvis from Iron Man. 
    Speak with polite formality, dry wit, and precision. Refer to yourself only as Canonflow, not Jarvis.
    """
)
human = HumanMessagePromptTemplate.from_template("{input}")
messages = [system, MessagesPlaceholder(variable_name="history"), human]
prompt = ChatPromptTemplate(messages=messages)

# ===== SETUP CHAIN =====
chain = prompt | LLM | StrOutputParser()
runnable_with_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)

st.title("A Simple Chatbot with Memory")
USER_ID = st.text_input("Enter your username", "User_1")

# If there are no chat history in session. then initialize
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

history = get_session_history(USER_ID)
previous_messages = history.get_messages()

# If there are previous messages, then load them
if len(previous_messages) > 0:
    st.session_state.chat_history = [
        {
            "role": msg.type,
            "content": msg.content
        }
        for msg in previous_messages
        if msg.type in ['human', 'ai']
    ]

# When the user want start new conversation
if st.button("Start New Conversation"):
    st.session_state.chat_history = []
    history = get_session_history(USER_ID)
    history.clear()

# ===== Display Chat History =====
for _message in st.session_state.chat_history:
    isFromHuman = True if _message['role'] == "human" else False

    if isFromHuman:
        message(_message['content'], is_user=isFromHuman, seed=63)
    else:
        # with st.chat_message(_message['role']):
        #     st.markdown(_message['content'])
        # with chat_message(_message['role']):
        #     st.markdown(_message['content'])
        with st.chat_message(_message['role']):
            st.markdown(_message["content"])

prompt = st.chat_input("What is up?")

# ===== IF THERE IS A PROMPT FROM USER =====
if prompt:
    # User
    st.session_state.chat_history.append({
        "role": 'human',
        'content': prompt
    })
    # with st.chat_message("human"):
    #     st.markdown(prompt)
    message(prompt, is_user=True, seed=63)

    # AI
    response = chat_with_llm(runnable_with_history, USER_ID, prompt)
    with st.chat_message("ai"):
        # st.markdown(response)
        response = st.write_stream(chat_with_llm(runnable_with_history, USER_ID, prompt))

    st.session_state.chat_history.append({
        "role": "ai",
        "content": response
    })
