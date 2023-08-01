import logging as logger
import streamlit as st
import os
import traceback
from utilities.LLMHelper import LLMHelper
from langchain import SerpAPIWrapper
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI

import os
import openai
from dotenv import load_dotenv

try:
    
    object_default = "oggetto della mail"
    body_default = "corpo della mail"
    
    st.title("Simulazione Mail Commercialista")

    llm_helper = LLMHelper()
    
    load_dotenv()
    openai.api_type = "azure"
    openai.api_base = os.getenv('OPENAI_API_BASE')
    openai.api_version = "2023-03-15-preview"
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
   
    functions= [  
    {
        "name": "search_hotels",
        "description": "Retrieves hotels from the search index based on the parameters provided",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The location of the hotel (i.e. Seattle, WA)"
                },
                "max_price": {
                    "type": "number",
                    "description": "The maximum price for the hotel"
                },
                "features": {
                    "type": "string",
                    "description": "A comma separated list of features (i.e. beachfront, free wifi, etc.)"
                }
            },
            "required": ["location"],
        },
    }]
        
    mail_object = st.text_input(label="Oggetto della mail:", value=object_default)
    mail_body = st.text_area(label="Corpo della mail:", value=body_default, height=300)
    
    messages= [ {"role": "user", "content": "Find beachfront hotels in San Diego for less than $300 a month with free breakfast."} ]

    response = openai.ChatCompletion.create(
        engine="gpt-35-turbo-0613",
        messages=messages,
        functions=functions,
        function_call="auto", 
    )

    print(response['choices'][0]['message'])
    
    
     
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