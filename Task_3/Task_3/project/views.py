from django.shortcuts import render, redirect
from .models import project
from .forms import ProjectForms
from django.views.generic import CreateView,DeleteView,UpdateView,DetailView,ListView
from django.contrib import messages
from .mixins import OwnerOrPermissionMixin
# def project_list(request):
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
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin

class Project_List(LoginRequiredMixin,ListView):
    model = project
    template_name = 'project/project_list.html'
    ordering = ['title']
    context_object_name = 'projects'

class Create_Project(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'project.add_project'
    model = project
    form_class = ProjectForms
    success_url = '/projects'
    template_name = 'project/create_project.html'
    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.description +='\n\nEND OF DESCRIPTION'
        messages.success(self.request, "Project created successfully!")        
        return super().form_valid(form)
class Project_Details(LoginRequiredMixin,DetailView):
    model = project
    context_object_name = 'project'
    template_name = 'project/project_detail.html'


class Project_Update(LoginRequiredMixin,OwnerOrPermissionMixin,UpdateView):
    required_permission = "project.change_project"    
    # owner_filed = ""
    model=project
    form_class = ProjectForms
    
    #permission_required = "project.change_project"
    success_url = "/projects"
    template_name = 'project/project_update.html'

class Project_Delete(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'project.delete_project'
    model = project
    success_url = '/projects'
    template_name = 'project/project_delete.html'
    context_object_name = 'project'