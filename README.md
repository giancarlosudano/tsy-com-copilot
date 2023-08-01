#Run everything locally in Python with venv
Please ensure you have Python 3.9+ installed.

#Create venv environment for Python:
python -m venv .venv
.venv\Scripts\activate

#Install PIP Requirements
pip install -r code\requirements.txt
Configure your .env as described in as described in Environment variables

#Run the WebApp
cd code
streamlit run OpenAI_Queries.py
