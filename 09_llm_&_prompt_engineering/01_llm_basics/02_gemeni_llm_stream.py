# pip install langchain_google_genai
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = GoogleGenerativeAI(
    model="gemini-1.5-flash", # give model name
    google_api_key="GOOGLE_API_KEY" # get GOOGLE_API_KEY from .env
    )

question = input("Enter you prompt: ")


for chunks in llm.stream(question): # stream -> give result in chunks
    print(chunks)