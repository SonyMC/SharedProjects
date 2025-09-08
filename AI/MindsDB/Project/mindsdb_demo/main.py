# MindsDB Interactive Question-Answering Demo
# This script creates a command-line interface for interacting with a MindsDB AI agent

import mindsdb_sdk

# Connect to the local MindsDB server
# Default MindsDB server runs on localhost port 47334
server = mindsdb_sdk.connect('http://127.0.0.1:47334')

# Access the default MindsDB project
# Projects in MindsDB organize databases, models, and agents
project = server.projects.get("mindsdb")

# Create a lambda function to generate SQL queries for the staging_agent
# The staging_agent appears to be a configured AI agent that answers questions
make_query_str = lambda question: f"SELECT answer from staging_agent where question = '{question}';"

# Main interaction loop - continuously prompt for questions until user exits
while True:
    # Get user input
    question = input("Ask a question: ")
    
    # Check for exit commands (case-insensitive)
    if question.lower() in ['exit', 'quit']:
        break
    
    # Generate the SQL query string using the user's question
    new_query_str = make_query_str(question)
    
    # Execute the query against the MindsDB project
    query = project.query(new_query_str)
    
    # Fetch the results from the query execution
    result = query.fetch()
    
    # Extract the answer from the first row of results
    # The staging_agent returns answers in the 'answer' column
    first_row_answer = result.iloc[0]['answer']
    
    # Display the answer to the user
    print(f"Answer: {first_row_answer}")

