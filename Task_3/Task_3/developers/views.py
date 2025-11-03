from django.shortcuts import render, redirect
from .models import Developer , Skill
from .forms import DeveloperForm , Skills_form
from django.views.generic import ListView,CreateView,DeleteView,DetailView,UpdateView
# def developer_list(request):
#     developers = Developer.objects.all()
#     return render(request,'developers/developer_list.html',{'developers':developers})

# def create_developers(request):
#     if request.method == 'POST':
#         form = DeveloperForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("developer_list")
#     else:
#         form = DeveloperForm()
#     return render(request,'developers/create_developer.html',{'form':form})

# def create_skill(request):
#     skills = Skill.objects.all()
#     if request.method == 'POST':
#         form = Skills_form(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("developer_list")
#     else:
#         form = Skills_form()
#     return render(request,"developers/create_skills.html",{'form':form,'skills':skills})
        
class Developers_List(ListView):
    model = Developer
    template_name = 'developers/developer_list.html'
    ordering= ['last_name']
    developers = Developer.objects.prefetch_related('skill').all()
    context_object_name = 'developers'
    def get_queryset(self):
        qs = Developer.objects.prefetch_related('skill').all()
        skill_param = (self.request.GET.get('skill') or '').strip()

        if skill_param:
            if skill_param.isdigit():
              qs = qs.filter(skill__id=int(skill_param)).distinct()
            else:
               qs = qs.filter(skill__title__icontains=skill_param).distinct()

        return qs

class Craate_Developers(CreateView):
    model = Developer
    form_class = DeveloperForm
    template_name = 'developers/create_developer.html'
    success_url = '/developers'
    
class Create_Skill(CreateView):
    model= Skill
    form_class = Skills_form
    template_name = 'developers/create_skills.html'
    success_url = '/developers'
    #context_object_name = 'skills'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['skills'] = Skill.objects.all()
        return context

class Developer_Detail(DetailView):
    model= Developer
    template_name = 'developers/developer_details.html'
    context_object_name = 'developer'


class Developer_Update(UpdateView):
    model = Developer
    #fields = ['age', 'email','skill']      
    #context_object_name = "developer"
    form_class = DeveloperForm
    success_url = '/developers'
    template_name = 'developers/developer_update.html'

    def get_form(self, form_class = None):
        form = super().get_form(form_class)
        form.fields = {k: v for k, v in form.fields.items() if k in ['email', 'age', 'skill']}
        return form

class Developer_Delete(DeleteView):
    model = Developer
    success_url = '/developers'
    template_name = 'developers/developer_delete.html'
    context_object_name = 'developer'


