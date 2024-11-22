from langchain_openai.chat_models import ChatOpenAI
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0.8)
