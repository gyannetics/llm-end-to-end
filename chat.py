"""
Streamlit UI for a Conversational Q&A Chatbot using LangChain and OpenAI.
"""

# Ensure that 'streamlit', 'langchain.schema', and 'langchain.chat_models' are installed in your environment
import streamlit as st
from langchain.schema import HumanMessage, AIMessage, SystemMessage
from langchain.chat_models import ChatOpenAI

def get_openai_response(question, chat_model):
    """
    Generates a response from OpenAI to the given question.

    Args:
        question (str): The question asked by the user.
        chat_model: The chat model instance.

    Returns:
        str: The AI-generated answer.
    """
    st.session_state['flow_messages'].append(HumanMessage(content=question))
    answer = chat_model(st.session_state['flow_messages'])
    st.session_state['flow_messages'].append(AIMessage(content=answer.content))
    return answer.content

# Streamlit UI setup
st.set_page_config(page_title="Conversational Q&A Chatbot")
st.header("Let's Chat")

# Initialize the chat model
chat_model = ChatOpenAI()

# Initialize session state for storing messages
if 'flow_messages' not in st.session_state:
    st.session_state['flow_messages'] = [
        SystemMessage(content=("You're a witty, sarcastic AI assistant who understands "
                               "human behavior."))
    ]

# User input
user_input = st.text_input("Write here:", key="input")

# Handle button click and display response
submit = st.button("What do you say?")
if submit and user_input:
    response = get_openai_response(user_input, chat_model)
    st.subheader("Hmmm... \n")
    st.write(response)
