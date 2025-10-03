from django.urls import path
from .import views


urlpatterns = [
    path("developers/",views.developer_list,name = "developer_list"),
    path("developers/new/",views.create_developers,name ="create_developer"),
    path("developers/skills/",views.create_skill,name ="create_skills")
]