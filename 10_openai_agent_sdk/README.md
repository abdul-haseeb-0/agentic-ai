# Basic OpenAI Agent SDK Example

This project demonstrates the use of the OpenAI Agent SDK to create a basic conversational agent. The agent is designed for educational purposes and showcases how to integrate OpenAI's language models into a Python application.

## Features

- **Agent Configuration**: Set up an agent with a name, instructions, and a specific model.
- **User Interaction**: Accept user queries via the command line.
- **Response Generation**: Generate responses using OpenAI's language model.
- **Error Handling**: Includes basic error handling for user input and API calls.

## Prerequisites

- Python 3.8 or higher
- An OpenAI API key with access to the Gemini model

## Setup

1. Clone this repository to your local machine.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set the `GEMINI_API_KEY` environment variable with your OpenAI API key:
   ```bash
   set GEMINI_API_KEY=your_api_key_here
   ```

## Usage

1. Run the script:
   ```bash
   python 01_basic_agent.py
   ```
2. Enter your query when prompted.
3. View the assistant's response in the console.

## Code Overview

- **01_basic_agent.py**: The main script that initializes the agent, handles user input, and generates responses.

## Educational Objectives

This project is intended to help learners:

- Understand the basics of integrating OpenAI's language models into Python applications.
- Learn how to handle user input and API responses.
- Explore the use of environment variables for secure API key management.

## License

This project is for educational purposes only and is not intended for production use.