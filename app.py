import streamlit as st 
import google.generativeai as genai

st.title("welcome to alex chat bot")

genai.configure(api_key="AIzaSyD0AJ42-kPJkv_dueFv8wS2xoXpOvnOtmU")

text = st.text_input("enter your question")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

if st.button("Search"):
   response = chat.send_message(text)
   st.write(response.text)