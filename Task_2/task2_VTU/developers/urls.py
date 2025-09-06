from  django.urls import path
from . import views
urlpatterns = [
    path("", views.developers_list,name = "developers_list"),
    path("developers/<str:username>/",views.developers_CV,name = "developers_CV")
]
