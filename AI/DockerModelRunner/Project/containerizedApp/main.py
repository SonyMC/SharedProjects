# Streamlit application for Docker Model Runner using OpenAI API
# This application allows users to interact with a model hosted on Docker Model Runner
# using the OpenAI API. It provides a simple chat interface for generating responses.
import  streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os




# #Open API endpoints  ( refer https://docs.docker.com/ai/model-runner/)
# GET /engines/llama.cpp/v1/models
# GET /engines/llama.cpp/v1/models/{namespace}/{name}
# POST /engines/llama.cpp/v1/chat/completions
# POST /engines/llama.cpp/v1/completions
# POST /engines/llama.cpp/v1/embeddings


# Load environment variables from .env file (like API keys)
load_dotenv()

# Instantiate the OpenAI client with the base URL
client = OpenAI(base_url=os.getenv("OPENAI_BASE_URL"), api_key=os.getenv("OPENAI_API_KEY"))

# Streamlit UI
st.title("Simple OpenAI Chatbot")
prompt = st.text_input("Enter your prompt:", 
                       "Why did the Indus Valley Civilization become extinct?")  


if st.button("Send"):
    with st.spinner("Generating response..."):
        # Prepare the chat message
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
        try:
            # Make the API call
            response = client.chat.completions.create(
                model=os.getenv("MODEL"),  # Use the model specified in the .env file
                messages=messages,
                temperature=0.7,
                max_tokens=150,
            )
            # Display the response
            st.write(response.choices[0].message.content)
            # st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")
# Display the model name
st.sidebar.header("Model Information")
st.sidebar.write(f"Using model: {os.getenv('MODEL')}")
st.sidebar.write(f"API Base URL: {os.getenv('OPENAI_BASE_URL')}")
