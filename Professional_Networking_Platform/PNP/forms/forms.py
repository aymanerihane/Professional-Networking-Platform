from django import forms
from ..models import User, Post, Cv
from django.contrib.auth.models import User as auth_user
from django.forms import SelectDateWidget

class MonthYearSelectWidget(SelectDateWidget):
    def __init__(self, *args, **kwargs):
        super(MonthYearSelectWidget, self).__init__(*args, **kwargs)
        self.format = '%Y-%m'  # Set the format to year-month


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


class CVForm(forms.ModelForm):
    company = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'Company'}))
    job_title = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'job_title'}))
    start_date = forms.CharField(required=False,max_length=100,
        widget=MonthYearSelectWidget(
            years=range(1980, 2025),
            empty_label=("Choose Year", "Choose Month", "Jour"),
        ),
    )
    end_date = forms.CharField(required=False,max_length=100,
        widget=forms.SelectDateWidget(years=range(1980, 2025), months={
            1: 'Janvier', 2: 'Février', 3: 'Mars', 4: 'Avril',
            5: 'Mai', 6: 'Juin', 7: 'Juillet', 8: 'Août',
            9: 'Septembre', 10: 'Octobre', 11: 'Novembre', 12: 'Décembre'
        }, empty_label=("Choisir l'année", "Choisir le mois", "Jour")),
        
    )
    school = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'School'}))
    degree = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'Degree'}))
    start_dateE = forms.CharField(required=False,
        widget=forms.SelectDateWidget(years=range(1980, 2025), months={
            1: 'Janvier', 2: 'Février', 3: 'Mars', 4: 'Avril',
            5: 'Mai', 6: 'Juin', 7: 'Juillet', 8: 'Août',
            9: 'Septembre', 10: 'Octobre', 11: 'Novembre', 12: 'Décembre'
        }, empty_label=("Choisir l'année", "Choisir le mois", "Jour")),
        )
    end_dateE = forms.CharField(required=False,
        widget=forms.SelectDateWidget(years=range(1980, 2025), months={
            1: 'Janvier', 2: 'Février', 3: 'Mars', 4: 'Avril',
            5: 'Mai', 6: 'Juin', 7: 'Juillet', 8: 'Août',
            9: 'Septembre', 10: 'Octobre', 11: 'Novembre', 12: 'Décembre'
        }, empty_label=("Choisir l'année", "Choisir le mois", "Jour")),

    )
    description = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'Experience description'}))
    class Meta:
        model = Cv
        fields = ['introduction', 'skills', 'languages','company', 'job_title', 'start_date', 'end_date', 'description','school', 'degree', 'start_dateE', 'end_dateE']

        widgets = {
            'introduction': forms.TextInput(attrs={'placeholder': 'Introduction'}),
            'skills': forms.TextInput(attrs={'placeholder': 'Skills'}),
            'languages': forms.TextInput(attrs={'placeholder': 'Languages'}),
        }





# class LoginForm(forms.Form):
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)