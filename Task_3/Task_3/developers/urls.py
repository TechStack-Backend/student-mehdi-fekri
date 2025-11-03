from django.urls import path
from .import views


urlpatterns = [
    path("developers/",views.Developers_List.as_view(),name = "developer_list"),
    path("developers/new/",views.Craate_Developers.as_view(),name ="create_developer"),
    path("developers/skills/",views.Create_Skill.as_view(),name ="create_skills"),
    path("developers/<int:pk>/",views.Developer_Detail.as_view(),name ="developer_details"),
    path("developers/<int:pk>/update",views.Developer_Update.as_view(),name ="developer_update"),
    path("developers/<int:pk>/delete",views.Developer_Delete.as_view(),name ="developer_delete")

]