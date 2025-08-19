
from openai import OpenAI
import os
from dotenv import load_dotenv





# #Open API endpoints  ( refer https://docs.docker.com/ai/model-runner/)
# GET /engines/llama.cpp/v1/models
# GET /engines/llama.cpp/v1/models/{namespace}/{name}
# POST /engines/llama.cpp/v1/chat/completions
# POST /engines/llama.cpp/v1/completions
# POST /engines/llama.cpp/v1/embeddings


# Load environment variables from .env file (like API keys)
load_dotenv()

# Define the Open API compliant API
BASE_URL = "http://localhost:12434/engines/llama.cpp/v1/"

# Instantiate the OpenAI client with the base URL
client = OpenAI(base_url=BASE_URL, api_key=os.getenv("OPENAI_API_KEY"))

# Define the model and the prompt
#model = "ai/gemma3n:4B-F16"  # Working model name
model = "ai/llama3.2"  # Another example model name
prompt = "Please write 500 words about why the Indus Valley Civilization became extinct."


# Prepare the chat message
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt}
]

# Create a chat completion using the new SDK style
response = client.chat.completions.create(
    model=model,                    # The AI model to use for generation
    messages=messages,              # The conversation history (system + user messages)
    temperature=0.7,                # Controls randomness (0.0 = deterministic, 1.0 = very random)
    max_tokens=256,                 # Maximum number of tokens to generate in the response
    stream=False                     # Whether to stream the response (False = wait for complete response)
)

# Print the model's reply
print(response.choices[0].message.content)
