from django.http import JsonResponse
import boto3
import json
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .launchdarkly_client import ld_client
from ldclient import Context
import textwrap
import logging

bedrock_client = boto3.client(
    service_name='bedrock-runtime',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('AWS_REGION')
)



def upload_api_document(request):
    if request.method == 'POST':
        # Logic to handle file upload will go here
        return JsonResponse({'message': 'API document uploaded successfully!'})
    return JsonResponse({'error': 'Invalid request method'}, status=400)


def health_check(request):
    if request.method == 'POST':
        # Logic to handle file upload will go here
        return JsonResponse({'message': 'Everything ghood!'})
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def generate_response(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('user_message', '')
        documentation = data.get('documentation', '')

        model_id = "meta.llama3-8b-instruct-v1:0"

        context = Context.builder("agent-instruction").build()
        instruction_flag = ld_client.variation("agent-instruction", context, "default_instruction")

        prompt = f"""
        <|begin_of_text|>
        <|start_header_id|>user<|end_header_id|>

        If the documentation is provided respond only with the python code. Don't add any string. Only write python code.
        Please respect the indentation since the code provided will directly be used with this method :

        exec(textwrap.dedent(model_response['generation']), exec_globals, exec_locals)

        {instruction_flag}

        Here is the user ask :

        {user_message}

        here is the provided documentation :

        {documentation}

        <|eot_id|>
        <|start_header_id|>assistant<|end_header_id|>

        """

        request = {
            "prompt": prompt
        }

        response = bedrock_client.invoke_model(body=json.dumps(request), modelId=model_id)
        model_response = json.loads(response["body"].read())

        if 'import' in model_response['generation']:

            exec_globals = {}
            exec_locals = {}

            model_response_str = str(model_response['generation'])
            cleaned_code = "\n".join(line.strip() for line in model_response_str.splitlines())


            exec(cleaned_code, exec_globals, exec_locals)

            # If you need to capture the output of the executed code, consider using exec with a custom namespace
            result = exec_locals

            return JsonResponse({'response': model_response})

        else:
            print("Documentation not provided")

        return JsonResponse({'response': model_response})
    return JsonResponse({'error': 'Invalid request method'}, status=400)