from .models import Developer
from django import forms


class DeveloperForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = ['first_name','last_name','email','age','skill']