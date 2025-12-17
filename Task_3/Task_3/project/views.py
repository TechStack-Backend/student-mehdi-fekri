from django.shortcuts import render, redirect
from .models import project
from .forms import ProjectForms
from django.views.generic import CreateView,DeleteView,UpdateView,DetailView,ListView
from django.contrib import messages# def project_list(request):
#     projects = project.objects.all()
#     return render(request,'project/project_list.html',{'projects':projects})

# def create_project(request):
#     if request.method == 'POST':
#         form = ProjectForms(request.POST)
#         if form.is_valid() :
#             form.save()
#             return redirect("project_list")
#     else:
#         form = ProjectForms()
#     return render(request,'project/create_project.html',{'form':form})
from django.contrib.auth.mixins import LoginRequiredMixin

class Project_List(LoginRequiredMixin,ListView):
    model = project
    template_name = 'project/project_list.html'
    ordering = ['title']
    context_object_name = 'projects'

class Create_Project(LoginRequiredMixin,CreateView):
    model = project
    form_class = ProjectForms
    success_url = '/projects'
    template_name = 'project/create_project.html'
    def form_valid(self, form):

        form.instance.description +='\n\nEND OF DESCRIPTION'
        messages.success(self.request, "Project created successfully!")        
        return super().form_valid(form)
class Project_Details(LoginRequiredMixin,DetailView):
    model = project
    context_object_name = 'project'
    template_name = 'project/project_detail.html'

class Project_Update(LoginRequiredMixin,UpdateView):
    model=project
    form_class = ProjectForms
    success_url = "/projects"
    template_name = 'project/project_update.html'

class Project_Delete(LoginRequiredMixin,DeleteView):
    model = project
    success_url = '/projects'
    template_name = 'project/project_delete.html'
    context_object_name = 'project'