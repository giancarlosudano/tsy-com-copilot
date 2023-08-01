import logging as logger
import streamlit as st
import os
import traceback
from utilities.LLMHelper import LLMHelper
from langchain import SerpAPIWrapper
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI

try:
    
    object_default = "oggetto della mail"
    body_default = "corpo della mail"
    
    st.title("Simulazione Mail Commercialista")

    llm_helper = LLMHelper()
    
    mrkl = initialize_agent(tools, llm_helper.llm, agent=AgentType.OPENAI_FUNCTIONS, verbose=True)
    
    mail_object = st.text_input(label="Oggetto della mail:", value=object_default)
    mail_body = st.text_area(label="Corpo della mail:", value=body_default, height=300)
     
    if st.button(label="Crea risposta"):
        prompt ="""Rispondi alla seguente mail delimitata da ###
###
Oggetto: {mail_object}
Mail: {mail_body}
###
"""
        prompt_complete = prompt.format(mail_object = mail_object, mail_body = mail_body)
        
        import langchain
        langchain.debug = True
        
        answer = mrkl.run(prompt_complete)
        st.success(answer)
        
except Exception as e:
    st.error(traceback.format_exc())