from django.shortcuts import render, redirect
from .models import Developer
from .forms import DeveloperForm
# Create your views here.
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
