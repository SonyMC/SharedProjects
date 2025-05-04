from langchain.embeddings.base import Embeddings  # Import base Embeddings class for type hints
from langchain_chroma import Chroma  # Import Chroma from langchain_chroma package for vector store functionality
from langchain.schema import BaseRetriever  # Import BaseRetriever for creating custom retrieval logic


class RedundantFilterRetriever(BaseRetriever):
    """
    A custom retriever that filters out redundant documents using Maximum Marginal Relevance (MMR).
    
    MMR attempts to maximize both relevance to the query and diversity among selected documents,
    reducing redundancy in search results.
    """
    embeddings: Embeddings  # The embedding model used to convert text to vectors. The value is set in the constructor.
    chroma: Chroma  # The Chroma vector store containing document embeddings . The value is set in the constructor.

    def get_relevant_documents(self, query):
        """
        Retrieve documents relevant to the query while reducing redundancy.
        
        Args:
            query (str): The user query to search for
            
        Returns:
            List[Document]: A list of documents relevant to the query with redundancy minimized
        """
        # Convert the query string into a vector embedding
        # i.e. calculate embeddings for the 'query' string
        emb = self.embeddings.embed_query(query)

        # Use Maximum Marginal Relevance (MMR) to find documents that are:
        # 1. Relevant to the query vector
        # 2. Diverse among themselves (reducing redundancy)
        return self.chroma.max_marginal_relevance_search_by_vector(
            embedding=emb,  # The vector representation of the query
            lambda_mult=0.8  # Controls diversity vs relevance tradeoff:
                             # Higher values (closer to 1.0) favor relevance to the query
                             # Lower values favor diversity among results
        )

    async def aget_relevant_documents(self):
        """
        Async version of get_relevant_documents - not implemented yet.
        
        Returns:
            List[Document]: Empty list placeholder
        """
        # Placeholder implementation for asynchronous retrieval
        # This would need to be implemented for async workflows
        return []
