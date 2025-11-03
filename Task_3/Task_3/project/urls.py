from django.urls import path
from .import views


urlpatterns = [
    path("",views.Project_List.as_view(),name = "project_list"),
    path("new/",views.Create_Project.as_view(),name ="create_project"),
    path("projects/<int:pk>/",views.Project_Details.as_view(),name ="project_detail"),
    path("projects/<int:pk>/update",views.Project_Update.as_view(),name ="project_update"),
    path("projects/<int:pk>/delete",views.Project_Delete.as_view(),name ="project_delete"),

]   