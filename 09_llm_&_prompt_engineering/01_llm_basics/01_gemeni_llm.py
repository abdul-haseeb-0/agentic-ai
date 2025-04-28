from langchain_google_genai import GoogleGenerativeAI

API_KEY = input("Enter your Google API Key: ")

llm = GoogleGenerativeAI(
     model="gemini-1.5-flash",
     google_api_key=API_KEY
)
query = input("Enter your query: ")
response = llm.invoke(query)

print(response)