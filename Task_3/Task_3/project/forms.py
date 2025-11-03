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
    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get('description')
        if not  description :
            raise forms.ValidationError("Description cannot be empty. ")
        return cleaned_data
     