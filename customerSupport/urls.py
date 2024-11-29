from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('resolve_request/<int:request_id>/', views.resolve_request, name='resolve_request'),
]
