from .models import Developer , Skill
from django import forms


class DeveloperForm(forms.ModelForm):
    skill = skill = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = Developer
        fields = ['first_name','last_name','email','age','skill']
        #fields['skill'] = forms.MultipleChoiceField()
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if  age < 18:
            raise  forms.ValidationError("Must be at least 18 years old.")
        return age
class Skills_form(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['title','description']
    