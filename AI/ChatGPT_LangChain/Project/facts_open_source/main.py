from langchain_community.document_loaders import TextLoader  # Import TextLoader from langchain_community package
from langchain.text_splitter import CharacterTextSplitter  # Import CharacterTextSplitter for splitting text into chunks
# from langchain_community.embeddings import HuggingFaceEmbeddings  # Import HuggingFaceEmbeddings for embedding text . This model is free and uses your local system resources
from langchain_huggingface import HuggingFaceEmbeddings # Import HuggingFaceEmbeddings for embedding text . This model is free and uses your local system resources
from dotenv import load_dotenv  # Import load_dotenv to load environment variables from a .env file

# Load environment variables (like API keys) from .env file
load_dotenv()

# Initialize HuggingFaceEmbeddings with sentence-transformers model
# This is used for converting text into vector representations locally
# The sentence-transformers models are specifically designed for generating high-quality embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",  # Using a popular sentence-transformers model
    model_kwargs={"device": "cpu"}  # Running on CPU, change to "cuda" if GPU is available
)

# Generate a vector representation of a sample text
sample_text = "This is a sample text for embedding."
# The embed_query method converts the text into a vector
sample_vector = embeddings.embed_query(sample_text)
# Print the generated vector
print(sample_vector)  # Output the vector representation of the sample text

# Initialize a text splitter with specific parameters
text_splitter = CharacterTextSplitter(
    separator="\n",  # Split the text at newline characters
    chunk_size=200,  # Each chunk will have a maximum of 200 characters
    chunk_overlap=0  # No overlap between consecutive chunks
)

# Initialize a TextLoader to load the content of the file "facts.txt"
loader = TextLoader("facts.txt")  # Specify the file path

# Load the document and split it into chunks in one operation
# This combines the loading and splitting steps for efficiency
docs = loader.load_and_split(
    text_splitter=text_splitter  # Use the previously defined text splitter
)

# Loop through each document chunk and print its content
for doc in docs:
    print(doc.page_content)  # Print the content of each chunk
    print("\n")  # Add two newlines after each chunk for better readability


