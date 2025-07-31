# Levenshtein Distance MCP Server

An MCP (Model Context Protocol) server that implements the Levenshtein Distance algorithm for calculating string similarity and edit distances.

## Overview

The Levenshtein distance is a string metric for measuring the difference between two sequences. It calculates the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one string into another.

## Features

This MCP server provides the following tools:

### Tools

1. **`calculate_levenshtein_distance`**
   - Calculate the basic Levenshtein distance between two strings
   - Returns: Integer representing the minimum edit distance

2. **`levenshtein_distance_with_matrix`**
   - Calculate distance with detailed matrix analysis
   - Returns: Distance, full DP matrix, and analysis information

3. **`levenshtein_similarity_ratio`**
   - Calculate similarity ratio (0.0 to 1.0) based on Levenshtein distance
   - Returns: Float representing similarity percentage

4. **`find_closest_match`**
   - Find the closest matching string from a list of candidates
   - Returns: Best match with distances and similarities for all candidates

5. **`edit_operations`**
   - Trace back the optimal sequence of edit operations
   - Returns: Step-by-step transformation operations

### Resources

1. **`levenshtein://algorithm-info`**
   - Detailed information about the Levenshtein Distance algorithm
   - Includes complexity analysis and applications

2. **`levenshtein://examples`**
   - Common examples and use cases
   - Demonstrates various transformation scenarios

## Installation

1. Ensure you have Python 3.11+ installed
2. Install dependencies:
   ```bash
   uv add fastmcp mcp[cli]
   ```

## Usage

### Running the Server

```bash
python main.py
```

### Example Tool Calls

#### Basic Distance Calculation
```python
# Calculate distance between "kitten" and "sitting"
result = calculate_levenshtein_distance("kitten", "sitting")
# Returns: 3
```

#### Detailed Analysis
```python
# Get full analysis with matrix
result = levenshtein_distance_with_matrix("cat", "bat")
# Returns: {
#   "distance": 1,
#   "matrix": [[0, 1, 2, 3], [1, 1, 2, 3], [2, 2, 1, 2], [3, 3, 2, 1]],
#   "str1": "cat",
#   "str2": "bat",
#   "analysis": "Minimum 1 edit(s) needed to transform 'cat' into 'bat'"
# }
```

#### Similarity Ratio
```python
# Calculate similarity ratio
ratio = levenshtein_similarity_ratio("hello", "jello")
# Returns: 0.8 (80% similar)
```

#### Find Closest Match
```python
# Find closest match from candidates
result = find_closest_match("test", ["best", "rest", "nest", "west"])
# Returns closest match with distances
```

#### Edit Operations
```python
# Get step-by-step transformation
ops = edit_operations("cat", "dog")
# Returns sequence of operations: substitute, substitute, substitute
```

## Algorithm Details

- **Time Complexity**: O(m × n) where m and n are string lengths
- **Space Complexity**: O(m × n) for the dynamic programming matrix
- **Method**: Dynamic programming with optimal substructure

## Applications

- Spell checking and correction
- DNA sequence analysis  
- Fuzzy string matching
- Data deduplication
- Plagiarism detection
- Autocomplete suggestions
- Search result ranking

## Examples

### Basic Usage
```
"cat" → "bat": Distance = 1 (substitute 'c' with 'b')
"kitten" → "sitting": Distance = 3
"hello" → "jello": Distance = 1
"" → "abc": Distance = 3 (insert all)
"test" → "": Distance = 4 (delete all)
```

### Complex Transformations
The server can handle complex string transformations and provide detailed step-by-step operations for educational and debugging purposes.

## License

This project is part of the MCP server collection for string processing algorithms.
