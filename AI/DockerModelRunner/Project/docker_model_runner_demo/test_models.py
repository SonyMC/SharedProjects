from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file (like API keys)
load_dotenv()

# Define the Open API compliant API
BASE_URL = "http://localhost:12434/engines/llama.cpp/v1/"

# Instantiate the OpenAI client with the base URL
client = OpenAI(base_url=BASE_URL, api_key=os.getenv("OPENAI_API_KEY"))

# Test different model names
model_names_to_try = [
    "ai/gemma3n:4B-F16",
    "ai/gemma3n",
    "gemma3n:4B-F16",
    "gemma3n",
    "ai/llama3.2:latest",
    "ai/llama3.2"
]

prompt = "Hello, please say hi back."

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt}
]

for model in model_names_to_try:
    print(f"\nTrying model: {model}")
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.7,
            max_tokens=50,
            stream=False
        )
        print(f"✅ SUCCESS with model: {model}")
        print(f"Response: {response.choices[0].message.content}")
        break  # Stop on first success
    except Exception as e:
        print(f"❌ Failed with model {model}: {e}")
        
print("\nDone testing models.")
