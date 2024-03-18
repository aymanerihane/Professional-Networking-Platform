from django import forms
from ..models import User, Post
from django.contrib.auth.models import User as auth_user

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['phone', 'address', 'city', 'country', 'cv', 'photo_profile', 'Visibility']

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs['placeholder'] = 'Phone'
        self.fields['address'].widget.attrs['placeholder'] = 'Address'
        self.fields['city'].widget.attrs['placeholder'] = 'City'
        self.fields['country'].widget.attrs['placeholder'] = 'Country'

class NewPost(forms.ModelForm):
    content = forms.CharField(label='content')
    class Meta:
        model = Post
        fields = ['content']


# class LoginForm(forms.Form):
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)