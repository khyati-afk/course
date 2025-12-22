import os
from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st

if "history" not in st.session_state:
    st.session_state.history = []
if "chat_starter" not in st.session_state:
    st.session_state.chat_started = False

load_dotenv(override=True) 
API_KEY = os.getenv("API_KEY")
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")
chat = model.start_chat(history=[])

st.sidebar.title("Chatbot")
st.sidebar.write("Hello, how can I help you?")
request = st.sidebar.text_input("Your message: ")
if(request):
    st.session_state.chat_started = True

if(st.session_state.chat_started):
    response = "default"
    try:
        # if request.strip() == "":
        #     bot_response = "Please enter a message."
        # else:
        api_response = chat.send_message(request)
        response = api_response.text
        pair = {'request':request, 'response':response}
        st.session_state.history.append(pair)

    except Exception as e:
        st.error(f"Error: {e}")

    for pair in st.session_state.history:
        st.info(pair['request'])
        st.write(pair['response'])


