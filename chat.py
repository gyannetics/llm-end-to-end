# from dotenv import load_dotenv
import streamlit as st
from langchain.schema import HumanMessage, AIMessage, SystemMessage
from langchain.chat_models import ChatOpenAI

# Streamlit UI

st.set_page_config(page_title="Conversational Q&A Chatbot")
st.header("Let's Chat")

chat = ChatOpenAI()
if 'flow_messages' not in st.session_state:
    st.session_state['flow_messages'] = [
        SystemMessage(
            content="You're an witty, sarcastic AI assistant who understands human behavior")
    ]


def get_openai_response(question):
    st.session_state['flow_messages'].append(HumanMessage(content=question))
    answer = chat(st.session_state['flow_messages'])
    st.session_state['flow_messages'].append(AIMessage(content=answer.content))
    return answer.content


input = st.text_input("Write here:", key="input")
response = get_openai_response(input)

submit = st.button("What do you say?")

if submit:
    st.subheader("Hmmm... \n")
    st.write(response)
