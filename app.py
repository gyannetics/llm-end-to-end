# Q & A Chatbot demo
from langchain.llms import OpenAI
from dotenv import load_dotenv
import streamlit as st
import os
load_dotenv()

# Function to load OpenAI model and get response


def get_openai_response(question):
    llm = OpenAI(model_name='text-davinci-003',
                 temperature=0.6,
                 openai_api_key=os.getenv('OPENAI_API_KEY'))
    response = llm(question)
    return response


st.set_page_config(page_title='Q&A Demo')
st.header("Simple Question and Answer App")

input = st.text_input("Write here:", key="input")
response = get_openai_response(input)

submit = st.button("What did you say?")

if submit:
    st.subheader("Hmmm... \n")
    st.write(response)
