from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Import the CustomUser model from the local models.py file
from .models import CustomUser

# --- Custom User Admin Configuration ---
class CustomUserAdmin(UserAdmin):
    # This defines the fields displayed in the admin interface

    # Custom fields for the change form
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

    # Custom fields for the list view
    list_display = ('email', 'username', 'is_staff', 'date_of_birth')

# Register the CustomUser model with the custom admin class
admin.site.register(CustomUser, CustomUserAdmin)
