from .import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('sign-up', views.sign_up, name="sign-up-page"),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='users-login-page'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='users-logout-page'),
]