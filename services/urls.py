from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_request, name='create_request'),
    path('request_details/<int:pk>/', views.requestDetails, name='request_detail'),
]
