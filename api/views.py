def to_serializable(obj):
    """Recursively convert objects to JSON-serializable types."""
    if isinstance(obj, dict):
        return {k: to_serializable(v) for k, v in obj.items()}
    elif isinstance(obj, (list, tuple)):
        return [to_serializable(v) for v in obj]
    elif hasattr(obj, "_asdict"):  # namedtuple
        return to_serializable(obj._asdict())
    elif hasattr(obj, "__dict__"):
        return to_serializable(vars(obj))
    elif hasattr(obj, "__str__") and not isinstance(obj, (str, bytes)):
        try:
            return str(obj)
        except Exception:
            return None
    else:
        return obj

from django.http import JsonResponse
import json
import os
from django.views.decorators.csrf import csrf_exempt
import textwrap
import logging
import sys
# Add the Sparkling Raincoat project root to sys.path for imports
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
from api_rotation.multi_api_rotation_provider import MultiAPIRotationProvider



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

        # Compose prompt for the LLM
        prompt = f"""
If the documentation is provided respond only with the python code. Don't add any string. Only write python code.
Please respect the indentation since the code provided will directly be used with this method:
exec(textwrap.dedent(model_response['generation']), exec_globals, exec_locals)

Here is the user ask:
{user_message}

Here is the provided documentation:
{documentation}
"""

        # Use the free API rotator
        rotator = MultiAPIRotationProvider(enable_rotation=True, debug=True)
        client, provider_name = rotator.get_client()
        try:
            # The client is expected to have a 'create' method (OpenAI-compatible)
            # We'll use a synchronous call for simplicity
            import asyncio
            from autogen_core.models._types import UserMessage
            response = asyncio.run(client.create(
                messages=[UserMessage(content=prompt, source="user")],
                extra_create_args={
                    "max_tokens": 1024,
                    "temperature": 0.2
                }
            ))
            model_response = to_serializable(response)
        except Exception as e:
            return JsonResponse({'error': f'LLM call failed: {str(e)}'}, status=500)

        # Optionally execute the code if desired (CAUTION: security risk)
        # For now, just return the generated code
        return JsonResponse({'response': model_response, 'provider': provider_name})
    return JsonResponse({'error': 'Invalid request method'}, status=400)