# Docker Model Runner Demo

This project demonstrates how to use Docker's Model Runner with Python to interact with AI models locally.

## Prerequisites

- Docker and Docker Compose installed
- At least 8GB of RAM (recommended for AI models)

## Quick Start

1. **Clone and navigate to the project:**
   ```bash
   cd docker_model_runner_demo
   ```

2. **Set up environment variables:**
   Make sure your `.env` file contains:
   ```
   OPENAI_API_KEY=your-api-key-here
   BASE_URL=http://localhost:12434/engines/llama.cpp/v1/
   ```

3. **Start the services:**
   ```bash
   docker-compose up -d model-runner
   ```
   Wait for the model runner to be healthy, then run:
   ```bash
   docker-compose up python-app
   ```

4. **For development with interactive shell:**
   ```bash
   docker-compose --profile dev up -d python-dev
   docker-compose exec python-dev bash
   ```

## Available Services

### model-runner
- Runs the Docker Model Runner service
- Exposes AI models on port 12434
- Includes health checks
- Persistent volumes for model data and cache

### python-app
- Runs the main Python application (`openai_version.py`)
- Connects to the model runner service
- One-time execution

### python-dev
- Development container with interactive shell
- Same environment as python-app but with bash access
- Use `--profile dev` to start

## Usage Examples

### Run the main script:
```bash
docker-compose up python-app
```

### Run the requests-based version:
```bash
docker-compose exec python-dev python main.py
```

### Run tests:
```bash
docker-compose exec python-dev python test_models.py
```

### Interactive development:
```bash
docker-compose --profile dev up -d python-dev
docker-compose exec python-dev bash
```

## Configuration

- Models are configured in the Python scripts
- Available models: `ai/llama3.2`, `ai/gemma3n`
- Base URL points to the model-runner service within the Docker network

## Troubleshooting

1. **Model runner not starting:** Check if you have enough RAM
2. **Connection refused:** Ensure model-runner service is healthy before starting python-app
3. **Permission issues:** The application runs as non-root user for security

## Cleanup

```bash
docker-compose down -v  # Remove containers and volumes
docker-compose down     # Remove containers only
```