import os
from langchain.llms import OpenAI
import streamlit as st
import pickle

with open('awesome.pkl', 'rb') as file:
    data = pickle.load(file)

os.environ["OPENAI_API_KEY"] =  data['openai_key']

# streamlit framework
st.title('**Ambresh Search Results**')

col1, col2 = st.columns(2)

with col1:
    input_text=st.text_input("**Search the topic you want**")

with col2:
    temp = st.slider('**Select Temperature**', 0.1, 1.0)

## OPENAI LLMS
llm=OpenAI(temperature=temp)

if input_text:
    st.write(llm(input_text))

