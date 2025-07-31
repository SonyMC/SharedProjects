# Projects Repository

This repository contains various AI projects, alongside other useful resources, tailored for the discerning consumer. Each project borrows inspiration and code from open-source repositories, with due attribution provided in the respective README.md files where applicable.

## Project Structure

### AI Projects
- **AWS Machine Learning**: Textract and Comprehend implementations
- **Azure AI**: Vision, NLP, Document Intelligence, Content Safety, and Custom Vision projects
- **ChatGPT & LangChain**: Integration projects with memory management and embedding techniques
- **HuggingFace**: Machine learning model implementations
- **MCP Servers**: Model Context Protocol server implementations
  - **Levenshtein Distance Server**: String similarity and edit distance calculations
  - **Simple MCP Server**: Basic FastMCP server with addition tools and dynamic greetings

### Other Projects
- **facefusion**: Face manipulation and fusion tools
- **n8n**: Workflow automation with Docker configuration

## MCP Server Projects

The `AI/MCP_Server/` directory contains Model Context Protocol (MCP) server implementations that provide specialized tools and resources for various computational tasks.

### Available MCP Servers

#### 1. Levenshtein Distance Server (`AI/MCP_Server/levenshtein_distance/`)
A comprehensive MCP server that implements the Levenshtein Distance algorithm for string similarity analysis.

**Features:**
- Calculate basic Levenshtein distance between strings
- Generate detailed transformation matrices
- Compute similarity ratios (0.0 to 1.0)
- Find closest matches from candidate lists
- Trace optimal edit operations step-by-step

**Use Cases:**
- Spell checking and correction
- DNA sequence analysis
- Fuzzy string matching
- Data deduplication
- Search result ranking

#### 2. Simple MCP Server (`AI/MCP_Server/simple_mcp_server/`)
A basic FastMCP server implementation serving as a foundation for MCP development.

**Features:**
- Addition tool for numeric calculations
- Dynamic greeting resources
- FastMCP framework demonstration

**Requirements:**
- Python 3.11+
- FastMCP 2.10.6+
- MCP CLI tools

**Running MCP Servers:**
```bash
cd AI/MCP_Server/[server_name]
python main.py
```

## How to Run

1. **Clone the Repository:**
   ```powershell
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```

2. **Read the Notes:**
   Each project contains either a notes.txt or refer.txt file, detailing setup steps and dependencies. Please review these files before proceeding.

3. **Follow Installation Steps:**
   Execute the commands as mentioned in the respective documentation.

### Special Instructions for MCP Servers

For MCP server projects (`AI/MCP_Server/`):

1. **Navigate to the specific server directory:**
   ```powershell
   cd AI/MCP_Server/levenshtein_distance
   # or
   cd AI/MCP_Server/simple_mcp_server
   ```

2. **Install dependencies using uv (recommended):**
   ```powershell
   uv add fastmcp mcp[cli]
   ```
   
   Or using pip:
   ```powershell
   pip install fastmcp "mcp[cli]"
   ```

3. **Run the MCP server:**
   ```powershell
   python main.py
   ```

4. **Test the server (if available):**
   ```powershell
   python test_server.py
   ```

## Important Notes

- This repository is optimized for Windows environments. Commands and tools used are designed with Windows in mind.
- If using a different platform, ensure necessary adjustments are made accordingly.
- Users are expected to exercise due diligence when adapting configurations to other operating systems.


## Troubleshooting

### General Issues
- **Dependency Issues**: If packages fail to install, refer to the specific project documentation for recommended versions or alternative dependencies.
- **Platform Compatibility**: If running on macOS/Linux, use equivalent commands (e.g., replace cmd instructions with Terminal alternatives).
- **Permission Errors**: Run terminal commands as Administrator if required (Run as Administrator option in Windows).

### MCP Server Specific Issues
- **Python Version**: Ensure Python 3.11+ is installed and active. Check with `python --version`
- **FastMCP Installation**: If FastMCP fails to install, try updating pip first: `pip install --upgrade pip`
- **uv Package Manager**: Install uv if not available: `pip install uv`
- **Server Connection**: Ensure the server is running on the correct port and protocol
- **Tool Registration**: Check that all tools and resources are properly decorated with `@mcp.tool()` and `@mcp.resource()`