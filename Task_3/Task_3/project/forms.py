from django import forms    
from .models import project, Developer


class ProjectForms(forms.ModelForm):
    developers = forms.ModelMultipleChoiceField(
        queryset= Developer.objects.all(),
        widget =  forms.CheckboxSelectMultiple,
        required=False,
    )
    class Meta:
        model = project
        fields = ['title','description','developers']
     