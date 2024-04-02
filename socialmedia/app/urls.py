from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.signin,name='signin'),
    path('signup',views.signup,name="signup"),
    path('homepage',views.homepage,name="homepage"),
    path('profile',views.profile,name="profile"),
    path('upload',views.upload,name='upload'),
    path('Logout',views.Logout,name="Logout"),
    path('like_post',views.like_post,name="like_post"),
    
]