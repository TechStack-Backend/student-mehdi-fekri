from .models import Developer , Skill
from django import forms


class DeveloperForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = ['first_name','last_name','email','age','skill']

class Skills_form(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['title','description']
    