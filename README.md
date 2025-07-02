# AutoAgent

AutoAgent is a tool designed to automatically create AI agents based on provided API documentation and user prompts. Leveraging Amazon Bedrock and LaunchDarkly, AutoAgent generates Python code to interact with APIs, dynamically adjusts instructions using feature flags, and can execute the generated code to automate workflows.

## Features

- Automatic AI Agent Generation
- Dynamic Instruction Adjustment with LaunchDarkly
- Code Execution for API Interaction

## Installation

1. Clone the repository:
```sh
git clone https://github.com/masmedim/autoagent.git
cd autoagent
```

2. Install dependencies :

```sh
pip install -r requirements.txt
```

3. Setup .env file

```env
AWS_ACCESS_KEY_ID=your_aws_access_key_id
AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
AWS_REGION=your_aws_region
LAUNCHDARKLY_SDK_KEY=your_launchdarkly_sdk_key
```

## Microservice Integration

AutoAgent is now a standalone microservice. To use as a submodule:

1. **Build Docker Image:**
   ```sh
   docker build -t autoagent:latest .
   ```
2. **Run Container:**
   ```sh
   docker run -d -p 8000:8000 --env-file .env autoagent:latest
   ```
3. **API Endpoint:**
   - POST `/api/generate-response/` (see below for request format)

4. **Submodule Usage:**
   - Add as a git submodule or copy the folder into your system's `services/` directory.
   - Integrate via HTTP API (recommended) or as a Python package if needed.

# Usage

1. Start the Django server:

```sh
python manage.py runserver
```

2. Use the following API endpoints:

```sh
POST /api/generate-response/
```

Request Body :

```json
{
  "user_message": "Your input text here",
  "documentation": "Your API documentation here"
}
```

## API Example

Request:
```json
{
  "user_message": "Your input text here",
  "documentation": "Your API documentation here"
}
```

Response:
```json
{
  "response": { ... },
  "provider": "GitHub Models | OpenRouter | Together AI"
}
```

## Requirements
- Python 3.11+
- Docker (optional, for containerized use)
- .env file with free LLM API keys (see below)

## .env Example
```
OPENROUTER_API_KEY=your_openrouter_key
TOGETHER_API_KEY=your_together_key
GITHUB_MODELS_API_KEY=your_github_models_key
```

# Microservice/submodule best practices checklist
- [x] Dockerfile present
- [x] README with API and integration instructions
- [x] .env example for free LLM providers
- [x] Automated server start script
- [x] VS Code task for dev workflow
- [x] No paid/external API dependencies
- [x] Remove deprecated configs/files (Bedrock, LaunchDarkly)
- [x] Confirm all endpoints documented
- [x] Confirm test coverage for endpoints

# Remove deprecated/unused configs
- [x] Remove Bedrock and LaunchDarkly from requirements.txt and settings.py
- [x] Remove api/launchdarkly_client.py if not used


