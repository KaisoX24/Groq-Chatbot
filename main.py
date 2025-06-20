from groq import Groq
import streamlit as st
import os
import time

client=Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def chat(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {'role': 'user', 'content': prompt},
            {'role': 'system', 'content': 'You are a helpful assistant.'}
            ],
        model="llama-3.1-8b-instant",
        max_tokens=1000,
        temperature=0.7,
    )
    return chat_completion.choices[0].message.content

def stream(prompt):
    full_response = ""
    placeholder = st.empty()
    for char in prompt:
        full_response += char
        placeholder.text(full_response)
        time.sleep(0.01)

st.set_page_config(page_title='Chat with Llama',page_icon='🦙',layout='wide')
st.title("Chat with Llama")
st.write("This is a simple chat application that uses the Groq API to interact with the Llama model. You can ask questions and get answers in real-time.")
st.write('---')

user_input=st.chat_input(placeholder='Type your message here...')

with st.spinner("Generating response..."):
    if user_input:
        response=chat(user_input)
        stream(response)
    else:
        st.write("Please enter a message to start the conversation.")