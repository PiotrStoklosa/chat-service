import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from openai import OpenAI

api_key = 'key'


@csrf_exempt
def send_message_and_get_response(request):
    body_unicode = request.body.decode('utf-8')
    data = json.loads(body_unicode)
    message = data['message']

    client = OpenAI(
        api_key=api_key
    )
    print(message)
    chat = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": message,
            }
        ],
        model="gpt-3.5-turbo",
    )

    answer = chat.choices[0].message.content
    print(answer)
    return JsonResponse({'message': message, 'response': answer})
