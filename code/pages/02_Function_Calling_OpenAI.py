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
import json
from dotenv import load_dotenv

def search_scadenze(nominativo: str):
    json_scadenze = """
{
  "results": [
    {
      "id": "932638c5-9888-462a-80e3-646ffa3778f5",
      "workspaceId": "0f5e7b71-f9e6-45bf-9747-859baa6469dd",
      "type": "f24",
      "scope": "fiscal_social_security",
      "description": {
        "title": "730",
        "details": "Pagamento 730"
      },
      "date": "2023-06-30T00:00:00.000Z",
      "totalAmount": 1254.67,
      "counterpart": {
        "taxId": "06363391001",
        "vatNumber": "06363391001",
        "description": "Agenzia delle Entrate",
        "partyId": "642aeeab7d46a85acaf9c16f"
      },
      "itemDetails": {
        "description": "AZIENDA TEST SCADENZE",
        "taxRegime": null
      },
      "currency": "EUR",
      "attachments": [
        {
          "id": "9f431f96-92b7-4607-b9cb-f94a91702fe9",
          "appId": null,
          "featureCode": null
        }
      ]
    },
    {
      "id": "432638c5-9888-462a-80e3-646ffa3778f5",
      "workspaceId": "0f5e7b71-f9e6-45bf-9747-859baa6469dd",
      "type": "f24",
      "scope": "fiscal_social_security",
      "description": {
        "title": "Debiti",
        "details": "rata 13 su 120"
      },
      "date": "2023-06-17T00:00:00.000Z",
      "totalAmount": 178.6,
      "counterpart": {
        "taxId": "06363391001",
        "vatNumber": "06363391001",
        "description": "Agenzia delle Entrate",
        "partyId": "642aeeab7d46a85acaf9c16f"
      },
      "itemDetails": {
        "description": "AZIENDA TEST SCADENZE",
        "taxRegime": null
      },
      "currency": "EUR",
      "attachments": [
        {
          "id": "4f431f96-92b7-4607-b9cb-f94a91702fe9",
          "appId": null,
          "featureCode": null
        }
      ]
    },
    {
      "id": "332638c5-9888-462a-80e3-646ffa3778f5",
      "workspaceId": "0f5e7b71-f9e6-45bf-9747-859baa6469dd",
      "type": "f24",
      "scope": "fiscal_social_security",
      "description": {
        "title": "Pagamento Debiti",
        "details": "rata 14 su 120"
      },
      "date": "2023-06-24T00:00:00.000Z",
      "totalAmount": 278.6,
      "counterpart": {
        "taxId": "06363391001",
        "vatNumber": "06363391001",
        "description": "Agenzia delle Entrate",
        "partyId": "642aeeab7d46a85acaf9c16f"
      },
      "itemDetails": {
        "description": "AZIENDA TEST SCADENZE",
        "taxRegime": null
      },
      "currency": "EUR",
      "attachments": [
        {
          "id": "6a431f96-92b7-4607-b9cb-f94a91702fe9",
          "appId": null,
          "featureCode": null
        }
      ]
    },
    {
      "id": "532638c5-9888-462a-80e3-646ffa3778f5",
      "workspaceId": "0f5e7b71-f9e6-45bf-9747-859baa6469dd",
      "type": "f24",
      "scope": "fiscal_social_security",
      "description": {
        "title": "Pagamento Debiti",
        "details": "rata 15 su 120"
      },
      "date": "2023-06-17T00:00:00.000Z",
      "totalAmount": 438.6,
      "counterpart": {
        "taxId": "06363391001",
        "vatNumber": "06363391001",
        "description": "Agenzia delle Entrate",
        "partyId": "642aeeab7d46a85acaf9c16f"
      },
      "itemDetails": {
        "description": "AZIENDA TEST SCADENZE",
        "taxRegime": null
      },
      "currency": "EUR"
    },
    {
      "id": "472638c5-9888-462a-80e3-646ffa3778f5",
      "workspaceId": "0f5e7b71-f9e6-45bf-9747-859baa6469dd",
      "type": "customer",
      "scope": "credit",
      "description": {
        "title": "Fattura emessa a A&E TELEVISION NETWORKS ITALY S.R.L.",
        "details": "Incasso fattura n. 2 del 03/04/2023",
        "data": {
          "docNumber": "2",
          "docDate": "2023-04-03T00:00:00.000Z"
        }
      },
      "date": "2023-04-27T00:00:00.000Z",
      "totalAmount": 158.6,
      "counterpart": {
        "taxId": "18155912159",
        "vatNumber": "18155912159",
        "description": "A&E TELEVISION NETWORKS ITALY S.R.L.",
        "partyId": "642aeeab7d46a85acaf9c16f"
      },
      "itemDetails": {
        "description": "AZIENDA TEST SCADENZE",
        "taxRegime": null
      },
      "currency": "EUR",
      "invoiceDate": "2023-04-03",
      "attachments": [
        {
          "id": "2e431f96-92b7-4607-b9cb-f94a91702fe9",
          "appId": "EIP",
          "featureCode": "SDI"
        }
      ]
    },
    
    {
      "id": "091f0784-0c86-4517-a009-202d99c80603",
      "workspaceId": "0f5e7b71-f9e6-45bf-9747-859baa6469dd",
      "type": "supplier",
      "scope": "debt",
      "description": {
        "title": "Fatture da pagare scadute",
        "details": "Fatture da pagare scadute"
      },
      "date": "2023-06-13T12:41:04.109Z",
      "totalAmount": -636,
      "counterpart": {
        "taxId": "14502302236",
        "vatNumber": "14502302236",
        "description": "AZIENDA Lynfa COLLEGATA ALLO STUDIO",
        "partyId": "646493227d46a85acaf9c22a"
      },
      "itemDetails": {
        "description": "AZIENDA TEST SCADENZE",
        "taxRegime": null
      },
      "currency": "EUR",
      "invoiceDate": null,
      "attachments": [
        {
          "id": "5ceb9e33-c803-453d-b77c-2cc1e2602340",
          "appId": "EIP",
          "featureCode": "ERCV"
        },
        {
          "id": "ed74bcd8-a12b-472a-9283-bdcdd2416ccf",
          "appId": "EIP",
          "featureCode": "ERCV"
        }
      ]
    },
    {
      "id": "6ee402f6-5188-4028-911f-e196046b3f5a",
      "workspaceId": "0f5e7b71-f9e6-45bf-9747-859baa6469dd",
      "type": "supplier",
      "scope": "debt",
      "description": {
        "title": "scadenze da pagare non scadute",
        "details": "scadenze da pagare non scadute"
      },
      "date": "2023-06-13T15:34:03.439Z",
      "totalAmount": -636.79,
      "counterpart": {
        "taxId": "14502302236",
        "vatNumber": "14502302236",
        "description": "AZIENDA Lynfa COLLEGATA ALLO STUDIO",
        "partyId": null
      },
      "itemDetails": {
        "description": "AZIENDA TEST SCADENZE",
        "taxRegime": null
      },
      "currency": "EUR",
      "invoiceDate": null,
      "paymentRegistryId": "62fa0ff1-5345-469a-bd4b-7d3b1113c804",
      "attachments": [
        {
          "id": "723f9393-be13-42c9-8e93-50e69a0d74d5",
          "appId": "EIP",
          "featureCode": "ERCV"
        },
        {
          "id": "a322e69a-cf33-4204-abe4-2f9b782d9ce4",
          "appId": "EIP",
          "featureCode": "ERCV"
        }
      ]
    },
    {
      "id": "b305bb83-c24e-40f9-9145-ef57a20874d4",
      "workspaceId": "0f5e7b71-f9e6-45bf-9747-859baa6469dd",
      "type": "supplier",
      "scope": "debt",
      "description": {
        "title": "Rata 1",
        "details": null
      },
      "date": "2023-06-13T15:49:44.503Z",
      "totalAmount": -673.58,
      "counterpart": {
        "taxId": "14502302236",
        "vatNumber": "14502302236",
        "description": "AZIENDA Lynfa COLLEGATA ALLO STUDIO",
        "partyId": "646493227d46a85acaf9c22a"
      },
      "itemDetails": {
        "description": "AZIENDA TEST SCADENZE",
        "taxRegime": null
      },
      "currency": "EUR",
      "invoiceDate": null,
      "paymentRegistryId": "6cb1c1f0-16d3-4a51-a7a5-38461091d241",
      "attachments": [
        {
          "id": "b9b8f81b-a6fb-451b-8d36-04970bed928c",
          "appId": "EIP",
          "featureCode": "ERCV"
        },
        {
          "id": "f19c7d5f-1146-4306-be14-00af742b9fc3",
          "appId": "EIP",
          "featureCode": "ERCV"
        }
      ]
    },
    
    {
      "id": "9fb17940-f0a8-443a-8680-ca4babbb6042",
      "workspaceId": "0f5e7b71-f9e6-45bf-9747-859baa6469dd",
      "type": "supplier",
      "scope": "debt",
      "description": {
        "title": "Rata 1",
        "details": null
      },
      "date": "2023-06-13T15:56:29.000Z",
      "totalAmount": -892.79,
      "counterpart": {
        "taxId": "14502302236",
        "vatNumber": "14502302236",
        "description": "AZIENDA Lynfa COLLEGATA ALLO STUDIO",
        "partyId": "646493227d46a85acaf9c22a"
      },
      "itemDetails": {
        "description": "AZIENDA TEST SCADENZE",
        "taxRegime": null
      },
      "currency": "EUR",
      "invoiceDate": null,
      "paymentRegistryId": "17e67a70-2bab-4109-a50e-16e87b550dc9",
      "attachments": [
        {
          "id": "4c44a310-2304-4ed8-891d-ea24f2b2b654",
          "appId": "EIP",
          "featureCode": "ERCV"
        },
        {
          "id": "29340f57-07b4-4487-af3a-0da54350b553",
          "appId": "EIP",
          "featureCode": "ERCV"
        },
        {
          "id": "7be396bc-f1f6-4061-a46a-460e8a5be8f3",
          "appId": "EIP",
          "featureCode": "ERCV"
        }
      ]
    },
    {
      "id": "8184c44a-e0f2-42de-aee0-e3cd103c5bc4",
      "workspaceId": "0f5e7b71-f9e6-45bf-9747-859baa6469dd",
      "type": "supplier",
      "scope": "debt",
      "description": {
        "title": "test",
        "details": "test"
      },
      "date": "2023-06-15T07:08:07.000Z",
      "totalAmount": -908.79,
      "counterpart": {
        "taxId": "14502302236",
        "vatNumber": "14502302236",
        "description": "AZIENDA Lynfa COLLEGATA ALLO STUDIO",
        "partyId": "646493227d46a85acaf9c22a"
      },
      "itemDetails": {
        "description": "AZIENDA TEST SCADENZE",
        "taxRegime": null
      },
      "currency": "EUR",
      "invoiceDate": null,
      "attachments": [
        {
          "id": "070c282b-ce84-4e5c-8736-ea115856515d",
          "appId": "EIP",
          "featureCode": "ERCV"
        },
        {
          "id": "ed74bcd8-a12b-472a-9283-bdcdd2416ccf",
          "appId": "EIP",
          "featureCode": "ERCV"
        },
        {
          "id": "7be396bc-f1f6-4061-a46a-460e8a5be8f3",
          "appId": "EIP",
          "featureCode": "ERCV"
        }
      ]
    },
    
    {
      "id": "b4315d1e-aaa3-42e3-9b40-adc125852145",
      "workspaceId": "0f5e7b71-f9e6-45bf-9747-859baa6469dd",
      "type": "supplier",
      "scope": "debt",
      "description": {
        "title": "Rata 2",
        "details": null
      },
      "date": "2023-06-19T15:49:53.000Z",
      "totalAmount": -200,
      "counterpart": {
        "taxId": "14502302236",
        "vatNumber": "14502302236",
        "description": "AZIENDA Lynfa COLLEGATA ALLO STUDIO",
        "partyId": "646493227d46a85acaf9c22a"
      },
      "itemDetails": {
        "description": "AZIENDA TEST SCADENZE",
        "taxRegime": null
      },
      "currency": "EUR",
      "invoiceDate": null,
      "paymentRegistryId": "04cb4ccd-f491-4109-8d60-0054e0a6ec95",
      "attachments": [
        {
          "id": "b9b8f81b-a6fb-451b-8d36-04970bed928c",
          "appId": "EIP",
          "featureCode": "ERCV"
        },
        {
          "id": "f19c7d5f-1146-4306-be14-00af742b9fc3",
          "appId": "EIP",
          "featureCode": "ERCV"
        }
      ]
    },
    
    {
      "id": "b92d2062-f432-4dec-b8c2-e9e62a8e4a1c",
      "workspaceId": "0f5e7b71-f9e6-45bf-9747-859baa6469dd",
      "type": "supplier",
      "scope": "debt",
      "description": {
        "title": "Rata 2",
        "details": null
      },
      "date": "2023-06-22T15:56:36.000Z",
      "totalAmount": -200,
      "counterpart": {
        "taxId": "14502302236",
        "vatNumber": "14502302236",
        "description": "AZIENDA Lynfa COLLEGATA ALLO STUDIO",
        "partyId": "646493227d46a85acaf9c22a"
      },
      "itemDetails": {
        "description": "AZIENDA TEST SCADENZE",
        "taxRegime": null
      },
      "currency": "EUR",
      "invoiceDate": null,
      "attachments": [
        {
          "id": "4c44a310-2304-4ed8-891d-ea24f2b2b654",
          "appId": "EIP",
          "featureCode": "ERCV"
        },
        {
          "id": "29340f57-07b4-4487-af3a-0da54350b553",
          "appId": "EIP",
          "featureCode": "ERCV"
        },
        {
          "id": "7be396bc-f1f6-4061-a46a-460e8a5be8f3",
          "appId": "EIP",
          "featureCode": "ERCV"
        }
      ]
    },
    {
      "id": "87e70963-b763-429e-a9d5-7b9dbcb662fc",
      "workspaceId": "0f5e7b71-f9e6-45bf-9747-859baa6469dd",
      "type": "customer",
      "scope": "credit",
      "description": {
        "title": "Raggruppamento con scadenze non scadute",
        "details": "Raggruppamento con scadenze non scadute"
      },
      "date": "2023-06-30T12:00:48.000Z",
      "totalAmount": 300,
      "counterpart": {
        "taxId": "09339391006",
        "vatNumber": "09339391006",
        "description": "BANCA NAZIONALE DEL LAVORO S.P.A. O IN FORMA CONTRATTA BNL S.P.A.",
        "partyId": "64885997c4b6a742fe38f43c"
      },
      "itemDetails": {
        "description": "AZIENDA TEST SCADENZE",
        "taxRegime": null
      },
      "currency": "EUR",
      "invoiceDate": null,
      "attachments": [
        {
          "id": "fda19556-9dab-4090-82fd-aee867e5aa65",
          "appId": "EIP",
          "featureCode": "SDI"
        }
      ]
    }
  ]
}
"""
    return json_scadenze

try:
    
    object_default = "oggetto della mail"
    body_default = "corpo della mail"
    
    st.title("Simulazione Mail Commercialista")

    llm_helper = LLMHelper()
    
    load_dotenv()
    openai.api_type = "azure"
    openai.api_base = os.getenv('OPENAI_API_BASE')
    openai.api_version = "2023-07-01-preview"
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    functions= [  
    {
        "name": "search_scadenze",
        "description": "Recupera dati di scadenze, pagamenti e altre informazioni sui clienti dell'assistente",
        "parameters": {
            "type": "object",
            "properties": {
                "nominativo": {
                    "type": "string",
                    "description": "La ragione sociale del cliente o il nome con cui verrà effettuata una ricerca sulle scadenze"
                }
            },
            "required": ["nominativo"],
        },
    }]
    
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
    
        messages= [
            {"role": "system", "content": "Sei l'assistente digitale di un commercialista. Aiuti a rispondere alle mail dei clienti con l'aiuto di dati che ti vengono forniti."}, 
            {"role": "user", "content": prompt_complete} ]

        response = openai.ChatCompletion.create(
            engine="gpt-35-turbo-16k",
            messages=messages,
            functions=functions,
            function_call="auto")
        
        response_message = response['choices'][0]['message']
        print(response_message)
        
        # Check if the model wants to call a function
        if response_message.get("function_call"):

            # Call the function. The JSON response may not always be valid so make sure to handle errors
            function_name = response_message["function_call"]["name"]

            available_functions = {
                "search_scadenze": search_scadenze,
            }
            
            function_to_call = available_functions[function_name] 

            function_args = json.loads(response_message["function_call"]["arguments"])
            function_response = function_to_call(**function_args)

            # Add the assistant response and function response to the messages
            messages.append( # adding assistant response to messages
                {
                    "role": response_message["role"],
                    "name": response_message["function_call"]["name"],
                    "content": response_message["function_call"]["arguments"],
                }
            )
            messages.append( # adding function response to messages
                {
                    "role": "function",
                    "name": function_name,
                    "content": function_response,
                }
            ) 

            # Call the API again to get the final response from the model
            second_response = openai.ChatCompletion.create(
                    messages=messages,
                    deployment_id="gpt-35-turbo-16k"
                    # optionally, you could provide functions in the second call as well
                )
            
            st.success(second_response["choices"][0]["message"])
        else:
            st.success(response["choices"][0]["message"])
                
except Exception as e:
    st.error(traceback.format_exc())