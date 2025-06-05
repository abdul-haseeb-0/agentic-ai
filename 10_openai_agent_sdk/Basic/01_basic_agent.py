from openai import AcyncOpenAI
from Agents import Agent, OpenAIChatCompletionModel, Runner
import os
from dotenv import load_dotenv

# Load the API key from environment variables for security
gemini_api_key = os.getenv('GEMINI_API_KEY')
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")

# Initialize the OpenAI client
client = AcyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Configure the agent with a name, instructions, and model
agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant.",
    model=OpenAIChatCompletionModel(model="gemini-2.0-flash", openai_client=client)
)

# Prompt the user for input
try:
    user_query = input("Enter Your Query: ")
    if not user_query.strip():
        raise ValueError("Query cannot be empty.")

    # Run the agent synchronously and get the result
    result = Runner.run_sync(agent, user_query)

    # Print the final output
    print("Assistant's Response:", result.final_output)
except Exception as e:
    print(f"An error occurred: {e}")