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


