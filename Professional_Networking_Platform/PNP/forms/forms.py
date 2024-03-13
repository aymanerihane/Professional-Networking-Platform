from django import forms
from ..models.users import User
from django.contrib.auth.models import User as auth_user

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['phone', 'address', 'city', 'country', 'cv', 'photo_profile', 'Visibility']

# class LoginForm(forms.Form):
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)