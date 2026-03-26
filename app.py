import streamlit as st
from prompts import SYSTEM_PROMPT
from bedrock_client import generate_response

st.set_page_config(
    page_title="AWS Study Copilot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AWS Study Copilot")
st.caption("Specialized assistant in RAG and LLMs using Amazon Bedrock")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "bedrock_messages" not in st.session_state:
    st.session_state.bedrock_messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Ask me about RAG, LLMs, embeddings, retrieval, chunking...")

if user_input:
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    st.session_state.bedrock_messages.append({
        "role": "user",
        "content": [{"text": user_input}]
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response_message = generate_response(
                    messages=st.session_state.bedrock_messages,
                    system_prompt=SYSTEM_PROMPT
                )

                assistant_text = ""
                for block in response_message["content"]:
                    if "text" in block:
                        assistant_text += block["text"]

                st.markdown(assistant_text)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": assistant_text
                })

                st.session_state.bedrock_messages.append({
                    "role": "assistant",
                    "content": [{"text": assistant_text}]
                })

            except Exception as e:
                st.error(f"Error while calling Bedrock: {str(e)}")

with st.sidebar:
    st.header("Options")

    if st.button("Clear conversation"):
        st.session_state.messages = []
        st.session_state.bedrock_messages = []
        st.rerun()
