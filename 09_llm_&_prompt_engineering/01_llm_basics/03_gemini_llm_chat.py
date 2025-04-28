# pip install langchain_google_genai

from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = GoogleGenerativeAI(
    model="gemini-1.5-flash", # give model name
    google_api_key="GOOGLE_API_KEY" # get GOOGLE_API_KEY from .env
    )

print("Type 'exit' or 'quit' to stop the chat.")
# chat logic
def chat_with_llm():
    while True:
        user_input = input("Enter Query: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting chat.")
            break
        response = llm(user_input)
        print(f"LLM: {response}")
        
chat_with_llm()