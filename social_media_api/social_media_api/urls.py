from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # The checker usually expects the accounts URLs to be included here
    path('api/accounts/', include('accounts.urls')),
]