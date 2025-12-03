from django.shortcuts import render
from django.views.generic import CreateView , UpdateView,DetailView
from .models import Profile 
from django.contrib.auth import login
from .forms import CreateUserForm , EditProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin


class RegisterUser(CreateView):
    template_name = 'accounts/register.html'
    form_class = CreateUserForm
    success_url = '/'
    def form_valid(self,form):
        response = super().form_valid(form)
        Profile.objects.create(user = self.object)
        login(self.request,self.object)
        return response
    

class EditProfileModel(LoginRequiredMixin,UpdateView):
    model = Profile
    template_name = 'accounts/edit_profile.html'
    form_class = EditProfileForm
    success_url = '/'

    def get_object(self):
        return self.request.user.profile
    

class Profile_Details(LoginRequiredMixin,DetailView):
    model = Profile
    template_name = 'accounts/mypage.html'
    context_object_name = 'userDetail'
    def get_object(self):
        return self.request.user.profile