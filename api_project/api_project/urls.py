# api_project/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token # Required import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    # This endpoint allows users to POST username/password and get a token
    path('api-token-auth/', obtain_auth_token), 
]