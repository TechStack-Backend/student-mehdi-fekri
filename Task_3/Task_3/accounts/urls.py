from django.urls import path
from .views import RegisterUser ,EditProfileModel , Profile_Details

urlpatterns = [
path('register/',RegisterUser.as_view(),name = 'register'),
path('ProfileEdit/',EditProfileModel.as_view(),name = 'edit_profile'),
path('mypage',Profile_Details.as_view(),name='mypage'),
]   