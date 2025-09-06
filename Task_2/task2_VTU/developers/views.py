from django.shortcuts import render
from django.http import  Http404
developers = [
    {
    "username" :"M84F",
    "first_name" :"mahdi",
    "last_name" : "fekri",
    "skills" : ["Python","C & C++"]
    },
        {
    "username" :"zahra66",
    "first_name" :"zahra",
    "last_name" : "hassnai",
    "skills" : ["C#","Docker"]
    },
     {
    "username" :"mohsen77",
    "first_name" :"mohsen",
    "last_name" : "javadi",
    "skills" : ["laravel","Java"]
    }

]

def developers_list(request):
    return  render(request,"developers/developers_list.html",{"developers" : developers})



def developers_CV(request,username):
    dev = None
    for d in developers:
        if d["username"] == username:
            dev = d
            break
    if dev is None:
        raise Http404("Developer Not Found!")
    return render(request,"developers/developers_CV.html",{"developer":dev})
    
