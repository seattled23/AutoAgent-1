from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_api_document, name='upload_api_document'),
    path('health_check/', views.health_check, name='Health Check'),
    path('generate-response/', views.generate_response, name='generate_response')
]
