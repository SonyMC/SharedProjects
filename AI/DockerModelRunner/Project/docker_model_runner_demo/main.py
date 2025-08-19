import requests

# #Open API endpoints  ( refer https://docs.docker.com/ai/model-runner/)
# GET /engines/llama.cpp/v1/models
# GET /engines/llama.cpp/v1/models/{namespace}/{name}
# POST /engines/llama.cpp/v1/chat/completions
# POST /engines/llama.cpp/v1/completions
# POST /engines/llama.cpp/v1/embeddings


# Define the Open API complaint API
url = "http://localhost:12434/engines/llama.cpp/v1/chat/completions"


data= {
    "model": "ai/llama3.2",
    #"model": "ai/gemma3n:4B-F16",
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Please write 500 words about why the Indus Valley Civilization became extinct"
        }
     ],
    # "temperature": 0.7,
    # "max_tokens": 256,
    # "stream": False
}


response = requests.post(url, json=data)
response.raise_for_status()  # Check for HTTP errors

# Print the model's reply
print(response.json()['choices'][0]['message']['content'])