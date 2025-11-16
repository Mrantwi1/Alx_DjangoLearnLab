# --- Imports at the top of views.py ---
# ... existing imports ...
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render # Ensure render is imported

# --- Helper Functions (Add these after your existing views) ---

def is_admin(user):
    """Checks for 'Admin' role access."""
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    """Checks for 'Librarian' role access."""
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    """Checks for 'Member' role access."""
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# --- Role-Based Views ---

@user_passes_test(is_admin)
def admin_view(request):
    """View accessible only by Admin."""
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    """View accessible only by Librarian."""
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    """View accessible only by Member."""
    return render(request, 'relationship_app/member_view.html')
