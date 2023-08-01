Run everything locally in Python with venv
This requires Redis running somewhere and expects that you've setup .env as described above. In this case, point REDIS_ADDRESS to your Redis deployment.

You can run a local Redis instance via:

 docker run -p 6379:6379 redis/redis-stack-server:latest
You can run a local Batch Processing Azure Function:

 docker run -p 7071:80 fruocco/oai-batch:latest
Please ensure you have Python 3.9+ installed.

Create venv environment for Python:

python -m venv .venv
.venv\Scripts\activate
Install PIP Requirements

pip install -r code\requirements.txt
Configure your .env as described in as described in Environment variables

Run the WebApp

cd code
streamlit run OpenAI_Queries.py
