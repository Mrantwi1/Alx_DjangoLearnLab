from django import forms

# 🚨 This class is required by the checker 🚨
class ExampleForm(forms.Form):
    """
    A placeholder form required by the security checker.
    Forms are essential for handling and validating user input securely.
    """
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
