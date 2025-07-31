"""
Levenshtein Distance MCP Server

This MCP server implements the Levenshtein Distance algorithm to calculate
the minimum number of single-character edits (insertions, deletions, or substitutions)
required to change one string into another.
"""
from mcp.server.fastmcp import FastMCP
from typing import List, Tuple

# Create an MCP server
mcp = FastMCP("Levenshtein Distance")


def levenshtein_distance_matrix(str1: str, str2: str) -> List[List[int]]:
    """
    Calculate the Levenshtein distance using dynamic programming matrix.
    Returns the full matrix for detailed analysis.
    """
    m, n = len(str1), len(str2)
    
    # Create a matrix with (m+1) x (n+1) dimensions
    matrix = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize the first row and column
    for i in range(m + 1):
        matrix[i][0] = i
    for j in range(n + 1):
        matrix[0][j] = j
    
    # Fill the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                cost = 0
            else:
                cost = 1
            
            matrix[i][j] = min(
                matrix[i-1][j] + 1,      # deletion
                matrix[i][j-1] + 1,      # insertion
                matrix[i-1][j-1] + cost  # substitution
            )
    
    return matrix


@mcp.tool()
def calculate_levenshtein_distance(str1: str, str2: str) -> int:
    """
    Calculate the Levenshtein distance between two strings.
    
    Args:
        str1: First string
        str2: Second string
    
    Returns:
        The minimum number of edits required to transform str1 into str2
    """
    if not str1 and not str2:
        return 0
    if not str1:
        return len(str2)
    if not str2:
        return len(str1)
    
    matrix = levenshtein_distance_matrix(str1, str2)
    return matrix[len(str1)][len(str2)]


@mcp.tool()
def levenshtein_distance_with_matrix(str1: str, str2: str) -> dict:
    """
    Calculate the Levenshtein distance and return detailed matrix information.
    
    Args:
        str1: First string
        str2: Second string
    
    Returns:
        Dictionary containing distance, matrix, and analysis
    """
    if not str1 and not str2:
        return {
            "distance": 0,
            "matrix": [[0]],
            "str1": str1,
            "str2": str2,
            "analysis": "Both strings are empty"
        }
    
    matrix = levenshtein_distance_matrix(str1, str2)
    distance = matrix[len(str1)][len(str2)]
    
    return {
        "distance": distance,
        "matrix": matrix,
        "str1": str1,
        "str2": str2,
        "analysis": f"Minimum {distance} edit(s) needed to transform '{str1}' into '{str2}'"
    }


@mcp.tool()
def levenshtein_similarity_ratio(str1: str, str2: str) -> float:
    """
    Calculate the similarity ratio between two strings based on Levenshtein distance.
    
    Args:
        str1: First string
        str2: Second string
    
    Returns:
        Similarity ratio between 0.0 (completely different) and 1.0 (identical)
    """
    max_len = max(len(str1), len(str2))
    if max_len == 0:
        return 1.0  # Both strings are empty
    
    distance = calculate_levenshtein_distance(str1, str2)
    similarity = 1.0 - (distance / max_len)
    return round(similarity, 4)


@mcp.tool()
def find_closest_match(target: str, candidates: List[str]) -> dict:
    """
    Find the closest matching string from a list of candidates.
    
    Args:
        target: The target string to match against
        candidates: List of candidate strings
    
    Returns:
        Dictionary with the best match, distance, and all candidates with their distances
    """
    if not candidates:
        return {
            "target": target,
            "best_match": None,
            "best_distance": None,
            "all_matches": []
        }
    
    results = []
    for candidate in candidates:
        distance = calculate_levenshtein_distance(target, candidate)
        similarity = levenshtein_similarity_ratio(target, candidate)
        results.append({
            "candidate": candidate,
            "distance": distance,
            "similarity": similarity
        })
    
    # Sort by distance (ascending)
    results.sort(key=lambda x: x["distance"])
    best_match = results[0]
    
    return {
        "target": target,
        "best_match": best_match["candidate"],
        "best_distance": best_match["distance"],
        "best_similarity": best_match["similarity"],
        "all_matches": results
    }


@mcp.tool()
def edit_operations(str1: str, str2: str) -> dict:
    """
    Trace back the optimal edit operations to transform str1 into str2.
    
    Args:
        str1: Source string
        str2: Target string
    
    Returns:
        Dictionary containing the sequence of edit operations
    """
    matrix = levenshtein_distance_matrix(str1, str2)
    operations = []
    
    i, j = len(str1), len(str2)
    
    while i > 0 or j > 0:
        if i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                # Characters match, no operation needed
                operations.append(f"Keep '{str1[i-1]}'")
                i -= 1
                j -= 1
            else:
                # Find which operation was used
                diag = matrix[i-1][j-1]  # substitution
                left = matrix[i][j-1] if j > 0 else float('inf')    # insertion
                up = matrix[i-1][j] if i > 0 else float('inf')      # deletion
                
                if diag <= left and diag <= up:
                    operations.append(f"Substitute '{str1[i-1]}' with '{str2[j-1]}'")
                    i -= 1
                    j -= 1
                elif left <= up:
                    operations.append(f"Insert '{str2[j-1]}'")
                    j -= 1
                else:
                    operations.append(f"Delete '{str1[i-1]}'")
                    i -= 1
        elif i > 0:
            operations.append(f"Delete '{str1[i-1]}'")
            i -= 1
        else:
            operations.append(f"Insert '{str2[j-1]}'")
            j -= 1
    
    operations.reverse()
    
    return {
        "str1": str1,
        "str2": str2,
        "distance": matrix[len(str1)][len(str2)],
        "operations": operations,
        "operation_count": len([op for op in operations if not op.startswith("Keep")])
    }


# Add a resource for algorithm information
@mcp.resource("levenshtein://algorithm-info")
def get_algorithm_info() -> str:
    """Information about the Levenshtein Distance algorithm"""
    return """
    Levenshtein Distance Algorithm
    
    The Levenshtein distance is a string metric for measuring the difference between two sequences.
    It is defined as the minimum number of single-character edits (insertions, deletions, or 
    substitutions) required to change one string into another.
    
    Time Complexity: O(m × n) where m and n are the lengths of the two strings
    Space Complexity: O(m × n) for the dynamic programming matrix
    
    Common Applications:
    - Spell checking and correction
    - DNA sequence analysis
    - Fuzzy string matching
    - Data deduplication
    - Plagiarism detection
    
    The algorithm uses dynamic programming to build a matrix where each cell [i,j] represents
    the minimum edits needed to transform the first i characters of string1 into the first j
    characters of string2.
    """


@mcp.resource("levenshtein://examples")
def get_examples() -> str:
    """Examples of Levenshtein Distance calculations"""
    return """
    Levenshtein Distance Examples:
    
    1. "cat" → "bat": Distance = 1 (substitute 'c' with 'b')
    2. "kitten" → "sitting": Distance = 3
       - Substitute 'k' with 's'
       - Substitute 'e' with 'i'
       - Insert 'g' at the end
    
    3. "hello" → "jello": Distance = 1 (substitute 'h' with 'j')
    4. "test" → "": Distance = 4 (delete all characters)
    5. "" → "abc": Distance = 3 (insert all characters)
    6. "same" → "same": Distance = 0 (no changes needed)
    
    The algorithm considers three operations:
    - Insertion: Add a character
    - Deletion: Remove a character  
    - Substitution: Replace a character
    """


if __name__ == "__main__":
    # Entry point for running the MCP server
    print("Levenshtein Distance MCP Server Starting...")
    print("Server: Levenshtein Distance")
    print("Transport: stdio")
    print("Available tools:")
    print("  - calculate_levenshtein_distance: Basic distance calculation")
    print("  - levenshtein_distance_with_matrix: Detailed analysis with matrix")
    print("  - levenshtein_similarity_ratio: Similarity percentage")
    print("  - find_closest_match: Find best match from candidates")
    print("  - edit_operations: Trace optimal edit sequence")
    print("Available resources:")
    print("  - levenshtein://algorithm-info: Algorithm information")
    print("  - levenshtein://examples: Usage examples")
    print("Server ready and listening for requests")
    print("-" * 50)
    
    mcp.run(transport='stdio')
