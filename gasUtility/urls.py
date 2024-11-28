from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('service/',include('services.urls')),
    path('support/',include('customerSupport.urls')),
]
