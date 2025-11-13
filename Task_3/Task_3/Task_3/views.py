from django.shortcuts import render, redirect
from django.views.generic import ListView,CreateView,DeleteView,DetailView,UpdateView



def home(request):
    return render(request,'home.html')