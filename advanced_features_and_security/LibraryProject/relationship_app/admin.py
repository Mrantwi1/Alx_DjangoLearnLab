from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book, Author, Library, Librarian # Import all your app models

# --- Custom User Admin (Step 4) ---
class CustomUserAdmin(UserAdmin):
    # Add the custom fields to the fieldsets for editing
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    # Add the custom fields to the list_display for the user table
    list_display = ('email', 'username', 'is_staff', 'date_of_birth')

    # Ensure the form handles the custom fields if you use custom forms, 
    # but for this task, fieldsets should be enough.

# Register the custom user model with the custom admin class
admin.site.register(CustomUser, CustomUserAdmin)

# You must also register your other models if they are not already.
# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(Library)
# admin.site.register(Librarian)
