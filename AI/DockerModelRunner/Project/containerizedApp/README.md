# Containerized Streamlit AI Chatbot

A Streamlit application that provides a simple chatbot interface using Docker Model Runner for AI model inference.

## Features

- Streamlit web interface for chatbot interactions
- Integration with Docker Model Runner for AI models
- Environment-based configuration
- Docker containerization with health checks
- Development and production profiles

## Prerequisites

- Docker and Docker Compose installed
- Docker Model Runner compatible AI models

## Quick Start

1. **Start the application:**
   ```bash
   docker-compose up -d
   ```

2. **Access the application:**
   - Streamlit app: http://localhost:8501
   - Model Runner API: http://localhost:12434

3. **Stop the application:**
   ```bash
   docker-compose down
   ```

## Development Mode

For development with hot reload:

```bash
docker-compose --profile dev up streamlit-dev
```

This will:
- Start the development version on port 8502
- Enable hot reload for code changes
- Mount the source code as a volume

## Configuration

The application uses environment variables defined in `.env`:

- `OPENAI_API_KEY`: API key for authentication (defaults to "dockermodelrunner")
- `OPENAI_BASE_URL`: Base URL for the AI model API
- `MODEL`: AI model to use (e.g., "ai/gemma3n:4B-F16")

## Services

### model-runner
- Runs the Docker Model Runner service
- Exposes AI models via OpenAI-compatible API
- Health checks ensure the service is ready

### streamlit-app
- Streamlit web application
- Depends on model-runner being healthy
- Provides chatbot interface

### streamlit-dev (development profile)
- Development version with hot reload
- Runs on port 8502
- Code changes are automatically reflected

## Health Checks

Both services include health checks:
- Model Runner: Checks `/health` endpoint
- Streamlit: Checks `/_stcore/health` endpoint

## Volumes

- `model-data`: Persistent storage for AI models
- `model-cache`: Cache for model operations

## Network

Services communicate via the `ai-network` bridge network.