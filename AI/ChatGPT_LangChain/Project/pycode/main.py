# This script generates a short code snippet based on a given task and programming language using OpenAI's ChatGPT model.
# It uses the LangChain library to create a prompt template and an LLM chain for generating the code.
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv
import argparse


# Load environment variables from .env file
# This is useful for managing sensitive information like API keys
load_dotenv()


# Create the chat model
llm = ChatOpenAI(temperature=0.7)  
# Initialize the ChatOpenAI model with a temperature of 0.7 for balanced creativity and determinism


# Set up argument parser to accept command-line arguments
parser = argparse.ArgumentParser()
#  Parse command-line arguments for task and language
# The default task is "return a list of numbers" and the default language is "python"
parser.add_argument("--language", default="python")  # Default programming language
parser.add_argument("--task", default="return a list of numbers")  # Default task description
#Parse the arguments from the command line
args = parser.parse_args()


# Define a prompt template for generating code
code_prompt = PromptTemplate(
    input_variables=["task", "language"],
    template="Write a very short {language} function that will {task}"
)

# Define a prompt template for generating test case
test_prompt = PromptTemplate(
    input_variables=["language", "code"],
    template="Write a test for the following {language} code:\n{code}"
)

# Create a parser to extract string outputs
output_parser = StrOutputParser()

# Create a runnable that generates code
code_chain = code_prompt | llm | output_parser

# Create the test generation flow
def generate_test(inputs):
    # Generate the code first
    code = code_chain.invoke(inputs)
    # Use the code to generate a test
    test_inputs = {"language": inputs["language"], "code": code}
    test = (test_prompt | llm | output_parser).invoke(test_inputs)
    # Return both code and test
    return {"code": code, "test": test}

# Generate the result by invoking the code generation flow
result = generate_test({
    "language": args.language,
    "task": args.task
})

# Print the generated code and test case
print(">>>>>> GENERATED CODE:")
print(result["code"])

print(">>>>>> GENERATED TEST:")
print(result["test"])


