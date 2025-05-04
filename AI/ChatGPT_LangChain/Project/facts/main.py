# This script demonstrates how to load a text file, split it into chunks, and perform a semantic similarity search using LangChain and Chroma.
from langchain_community.document_loaders import TextLoader  # Import TextLoader from langchain_community package
from langchain.text_splitter import CharacterTextSplitter  # Import CharacterTextSplitter for splitting text into chunks
from langchain_openai import OpenAIEmbeddings  # Import OpenAIEmbeddings from openai-specific package
from langchain_chroma import Chroma # Import Chroma from langchain_chroma package
from dotenv import load_dotenv  # Import load_dotenv to load environment variables from a .env file

# Load environment variables from .env file (contains OpenAI API key)
load_dotenv()

# Initialize OpenAI embeddings model
# This model converts text into vector representations that capture semantic meaning
embeddings = OpenAIEmbeddings()

# Create a text splitter with specific parameters for document processing
text_splitter = CharacterTextSplitter(
    separator="\n",     # Split text at newline characters
    chunk_size=200,     # Each chunk will have maximum 200 characters
    chunk_overlap=0     # No overlap between consecutive chunks
)

# Create a text loader to read the facts.txt file
loader = TextLoader("facts.txt")

# Load the document and split it into chunks in a single operation
docs = loader.load_and_split(
    text_splitter=text_splitter  # Use the previously defined text splitter
)

# Create a Chroma vector database from the document chunks
db = Chroma.from_documents(
    docs,                    # The document chunks to store in the database
    embedding=embeddings,    # The embedding model to convert text to vectors
    persist_directory="emb"  # Directory to store the vector database
)

# Perform a semantic similarity search on the vector database
results = db.similarity_search(
    "What is an interesting fact about the English language?"  # The search query
)

# Iterate through search results and print each matching document
for result in results:
    print("\n")                  # Print a blank line for readability
    print(result.page_content)   # Print the content of the matching document
