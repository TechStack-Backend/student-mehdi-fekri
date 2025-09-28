from django.urls import path
from .import views


urlpatterns = [
    path("developers/",views.developer_list,name = "developer_list"),
    path("developers/new/",views.create_developers,name ="create_developer")
]