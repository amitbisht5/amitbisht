
from django.urls import path
from . import  views


app_name = 'profiles'
urlpatterns = [

    path('', views.profile_view, name='profile'),
    path('update/', views.update_profile, name='update')
]
