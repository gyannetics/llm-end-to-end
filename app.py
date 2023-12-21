"""
Streamlit UI for a Q&A Chatbot using LangChain and OpenAI.
"""

import os
from dotenv import load_dotenv
import streamlit as st
from langchain.llms import OpenAI

# Load environment variables
load_dotenv()


def get_openai_response(question):
    """
    Generates a response from OpenAI to the given question.

    Args:
        question (str): The question asked by the user.

    Returns:
        str: The AI-generated answer.
    """
    llm = OpenAI(openai_api_key=os.getenv('OPENAI_API_KEY'), model_name='text-davinci-003')

    openai_response = llm(question)

    return openai_response


# Streamlit UI setup
st.set_page_config(page_title='Q&A Demo')
st.header("Simple Question and Answer App")

# User input
user_input = st.text_input("Write here:", key="input")

# Handle button click and display response
submit = st.button("What did you say?")
if submit and user_input:
    response = get_openai_response(user_input)
    st.subheader("Hmmm... \n")
    st.write(response)
