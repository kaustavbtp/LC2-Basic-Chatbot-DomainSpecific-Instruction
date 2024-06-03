from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()


os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")



prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a Experienced SAP BTP CAPM (Nodejs) CDS Developer. Please response to the BTP technical related question only"),
        ("user","Question:{question}")
    ]
)


# streamlit framework

st.title('Langchain With OPENAI')
input_text=st.text_input("You can ask anything")
# give me a sample project structure

# openAI LLm 
llm=ChatOpenAI()
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))