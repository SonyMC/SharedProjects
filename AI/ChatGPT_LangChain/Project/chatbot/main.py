from langchain_core.prompts import MessagesPlaceholder, HumanMessagePromptTemplate, ChatPromptTemplate
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory, FileChatMessageHistory
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

def create_chatbot():
    """
    Creates and initializes the chatbot with the OpenAI model, 
    prompt template and conversation memory.
    """
    # Initialize the ChatOpenAI model
    chat = ChatOpenAI(
        temperature=0.7,  # Controls randomness of outputs - 0.7 gives creative but relevant responses
        model_name="gpt-3.5-turbo"  # Using gpt-3.5-turbo for good balance of performance and cost
    )
    
    # Set up memory to store conversation history
    memory = ConversationBufferMemory(
        chat_memory=FileChatMessageHistory("messages.json"),  # Store chat history in a JSON file
        memory_key="messages",  # Key to access the conversation history in memory
        return_messages=True  # Return the full conversation history when accessed
    )
    
    # Create a chat prompt template
    prompt = ChatPromptTemplate(
        input_variables=["content", "messages"],  # Variables to replace in the template
        messages=[
            # Placeholder for the conversation history
            MessagesPlaceholder(variable_name="messages"),
            # Template for human messages
            HumanMessagePromptTemplate.from_template("{content}")
        ]
    )
    
    # Combine model, prompt, and memory into a chain
    chain = LLMChain(
        llm=chat,
        prompt=prompt,
        memory=memory,
        verbose=True  # Set to True to see the prompts being sent to the model
    )
    
    return chain

def run_chatbot():
    """
    Main function to run the chatbot in an interactive loop
    """
    print("Welcome to the ChatBot! Type 'exit' to end the conversation.")
    chain = create_chatbot()
    
    while True:
        content = input("You: ")
        
        if content.lower() in ["exit", "quit", "bye"]:
            print("ChatBot: Goodbye! Have a great day!")
            break
            
        try:
            # Process the user input and get response
            result = chain({"content": content})
            print(f"ChatBot: {result['text']}")
        except Exception as e:
            print(f"Error: {str(e)}")
            print("An error occurred. Please try again.")

if __name__ == "__main__":
    run_chatbot()

