from langchain_core.prompts import MessagesPlaceholder, HumanMessagePromptTemplate, ChatPromptTemplate
from langchain_core.runnables.history import RunnableWithMessageHistory
# from langchain_community.chat_models import ChatOllama
from langchain_ollama import ChatOllama
from langchain.memory import ConversationBufferMemory, FileChatMessageHistory
from dotenv import load_dotenv
import os


def create_chatbot():
    """
    Creates and initializes the chatbot with an open-source model (via Ollama),
    prompt template and conversation memory.
    """
    # Initialize the ChatOllama model
    chat = ChatOllama(
        temperature=0.7,  # Controls randomness of outputs
        model="llama3"  # Specify the Ollama model name (e.g., llama3, mistral)
    )

    # Create a chat prompt template
    prompt = ChatPromptTemplate(
        input_variables=["content"], # Removed "messages" as RunnableWithMessageHistory handles it
        messages=[
            # Placeholder for the conversation history
            MessagesPlaceholder(variable_name="history"), # Use "history" as expected by RunnableWithMessageHistory
            # Template for human messages
            HumanMessagePromptTemplate.from_template("{content}")
        ]
    )

    # Combine model and prompt using RunnableSequence syntax
    runnable = prompt | chat

    # Wrap the runnable with message history management
    chain_with_history = RunnableWithMessageHistory(
        runnable,
        lambda session_id: FileChatMessageHistory(f"{session_id}_messages.json"), # Use session_id in filename
        input_messages_key="content",
        history_messages_key="history",
    )

    return chain_with_history

def run_chatbot():
    """
    Main function to run the chatbot in an interactive loop
    """
    print("Welcome to the ChatBot! Type 'exit' to end the conversation.")
    chain = create_chatbot()
    session_id = "user_session_1" # Example session ID, could be dynamic

    while True:
        content = input("You: ")

        if content.lower() in ["exit", "quit", "bye"]:
            print("ChatBot: Goodbye! Have a great day!")
            break

        try:
            # Process the user input and get response using invoke
            # Pass the config with the session_id
            result = chain.invoke(
                {"content": content},
                config={"configurable": {"session_id": session_id}}
            )
            # The result is now the direct response content (AIMessage object)
            print(f"ChatBot: {result.content}")
        except Exception as e:
            print(f"Error: {str(e)}")
            print("An error occurred. Please try again.")

if __name__ == "__main__":
    run_chatbot()

