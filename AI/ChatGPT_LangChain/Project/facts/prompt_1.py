# This script demonstrates how to use LangChain with a Chroma vector database to perform a semantic similarity search and generate answers to questions.

from langchain_chroma import Chroma # Import Chroma from langchain_chroma package
from langchain_openai import OpenAIEmbeddings  # Import OpenAIEmbeddings from openai-specific package
from langchain.chains import RetrievalQA  # Import RetrievalQA chain for question answering
from langchain_openai import ChatOpenAI  # Import ChatOpenAI from openai-specific package
from dotenv import load_dotenv  # Import load_dotenv to load environment variables
from redundant_filter_retriever import RedundantFilterRetriever  # Import custom retriever for filtering redundant documents
import langchain # Import langchain for various utilities

langchain.debug = True  # Enable debug mode for LangChain to get detailed logs

# Load environment variables (typically contains API keys like OPENAI_API_KEY)
load_dotenv()

# Initialize the ChatOpenAI model for generating responses
chat = ChatOpenAI(temperature=0)  # Set temperature to 0 for more deterministic responses

# Initialize OpenAI embeddings model to convert text to vector representations
embeddings = OpenAIEmbeddings()

# Load the existing Chroma vector database from the "emb" directory
# This database contains document vectors previously created using the same embedding function
db = Chroma(
    persist_directory="emb",  # Directory where the vector database is stored
    embedding_function=embeddings  # Use the same embedding function that created the database
)

# Verify if the database has documents
docs_count = db._collection.count()
if docs_count == 0:
    raise ValueError("No documents found in the vector database. Please make sure you've loaded documents first.")

print(f"Database contains {docs_count} documents")

# Create a retriever from the vector database with search parameters
# retriever = db.as_retriever(
#     search_type="similarity",  # Use similarity search
#     search_kwargs={"k": 4}  # Return top 4 documents
# )

# Create a custom retriever that reduces redundancy in search results
retriever = RedundantFilterRetriever(
    embeddings=embeddings,  # Pass the embedding model to convert queries to vectors
    chroma=db  # Pass the Chroma vector store containing our document embeddings
)

# Create a RetrievalQA chain that combines document retrieval with question answering
chain = RetrievalQA.from_chain_type(
    llm=chat,  # The language model to use for answering questions
    retriever=retriever,  # The retriever to use for finding relevant documents
    verbose=True,  # If True, prints detailed information about the chain's operations
    chain_type="stuff"  # Using "stuff" as it's more reliable than map_rerank
    #chain_type="map_reduce"  # map_reduce is less reliable than stuff
    #chain_type="map_rerank"  # map_rerank is less reliable than stuff
    #chain_type="refine"  # refine is less reliable than stuff
)

# Run the chain with a query about English language facts
try:
    # This will retrieve relevant documents and then generate an answer based on those documents
    result = chain.invoke("What is an interesting fact about the English language?")
    # Print the generated answer
    print("\nFinal Answer:")
    print(result["result"])
except Exception as e:
    print(f"An error occurred: {e}")
    # Try a direct retrieval to diagnose issues
    print("\nAttempting direct document retrieval:")
    docs = retriever.get_relevant_documents("What is an interesting fact about the English language?")
    if docs:
        print(f"Retrieved {len(docs)} documents directly")
        for i, doc in enumerate(docs):
            print(f"\nDocument {i+1}:")
            print(doc.page_content)
    else:
        print("No documents retrieved. The database may be empty or the embeddings may not match.")
