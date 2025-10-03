from django.shortcuts import render, redirect
from .models import Developer , Skill
from .forms import DeveloperForm , Skills_form

def developer_list(request):
    developers = Developer.objects.all()
    return render(request,'developers/developer_list.html',{'developers':developers})

def create_developers(request):
    if request.method == 'POST':
        form = DeveloperForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("developer_list")
    else:
        form = DeveloperForm()
    return render(request,'developers/create_developer.html',{'form':form})

def create_skill(request):
    skills = Skill.objects.all()
    if request.method == 'POST':
        form = Skills_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("developer_list")
    else:
        form = Skills_form()
    return render(request,"developers/create_skills.html",{'form':form,'skills':skills})
        
