from django.urls import path

from .chat import send_message_and_get_response

urlpatterns = [
    path('chat', send_message_and_get_response, name='send_message_and_get_response'),
]
