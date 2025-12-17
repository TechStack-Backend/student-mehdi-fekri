from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile
from django.forms import FileInput

class CreateUserForm(UserCreationForm):
    pass


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','picture']
        widgets = {
            'picture': forms.FileInput() 
        }