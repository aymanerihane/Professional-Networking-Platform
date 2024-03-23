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
            'skills': forms.TextInput(attrs={'placeholder': 'Skills(separeted by , ex: HTML, CSS, JavaScript)'}),
            'languages': forms.TextInput(attrs={'placeholder': 'Languages(separeted by , ex: English, French, Spanish)'}),
        }


class EditCV(forms.ModelForm):
    # if the cv is already exist show it avec le nom du fichier
    cv = forms.FileField(required=True, label='CV')
    class Meta:
        model = User
        fields = ['cv']

class EditProfile(forms.ModelForm):
    username = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(max_length=100, required=False, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    old_password = forms.CharField(max_length=100, required=False, widget=forms.PasswordInput(attrs={'placeholder': 'Old Password'}))
    new_password = forms.CharField(max_length=100, required=False, widget=forms.PasswordInput(attrs={'placeholder': 'New Password'}))
    class Meta:
        model = User
        fields = ['username','email','old_password','new_password','photo_profile','phone', 'address', 'city', 'country', 'Visibility']

    widgets = {
        'phone': forms.TextInput(attrs={'placeholder': 'Phone'}),
        'address': forms.TextInput(attrs={'placeholder': 'Address'}),
        'city': forms.TextInput(attrs={'placeholder': 'City'}),
        'country': forms.TextInput(attrs={'placeholder': 'Country'}),
        }

#form to update user profile

##etid user info
# class EditUserForm(forms.ModelForm):
#     class Meta:
#         model = User, auth_user
#         fields = ['username','phone', 'address', 'city', 'country', 'cv', 'photo_profile', 'Visibility']

#     def __init__(self, *args, **kwargs):
#         super(EditUserForm, self).__init__(*args, **kwargs)
#         self.fields['username'].widget.attrs['placeholder'] = 'Username'
#         self.fields['phone'].widget.attrs['placeholder'] = 'Phone'
#         self.fields['address'].widget.attrs['placeholder'] = 'Address'
#         self.fields['city'].widget.attrs['placeholder'] = 'City'
#         self.fields['country'].widget.attrs['placeholder'] = 'Country'

##add experience
class ExperienceForm(forms.ModelForm):
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
    description = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'Experience description'}))
    class Meta:
        model = Cv
        fields = ['company', 'job_title', 'start_date', 'end_date', 'description']

#add education
class EducationForm(forms.ModelForm):
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
    class Meta:
        model = Cv
        fields = ['school', 'degree', 'start_dateE', 'end_dateE']
        widgets = {
            'school': forms.TextInput(attrs={'placeholder': 'School'}),
            'degree': forms.TextInput(attrs={'placeholder': 'Degree'}),
        }

#add skills
class SkillsForm(forms.ModelForm):
    class Meta:
        model = Cv
        fields = ['skills']
        widgets = {
            'skills': forms.TextInput(attrs={'placeholder': 'Skills(separeted by , ex: HTML, CSS, JavaScript)'}),
        }

#add languages
class LanguagesForm(forms.ModelForm):
    class Meta:
        model = Cv
        fields = ['languages']
        widgets = {
            'languages': forms.TextInput(attrs={'placeholder': 'Languages(separeted by , ex: English, French, Spanish)'}),
        }

class AboutForm(forms.ModelForm):
    class Meta:
        model = Cv
        fields = ['about']
        widgets = {
            'about': forms.Textarea(attrs={'placeholder': 'About'}),
        }