from django import forms
from .users import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'phone', 'address', 'city', 'country', 'cv', 'photo_profile', 'Visibility']  

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)