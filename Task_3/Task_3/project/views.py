from django.shortcuts import render, redirect
from .models import project
from .forms import ProjectForms
def project_list(request):
    projects = project.objects.all()
    return render(request,'projects/project_list.html',{'projects':projects})

def create_project(request):
    if request.method == 'POST':
        form = ProjectForms(request.POST)
        if form.is_valid() :
            form.save()
            return redirect("project_list")
    else:
        form = ProjectForms()
    return render(request,'projects/create_projects.html',{'form':form})
