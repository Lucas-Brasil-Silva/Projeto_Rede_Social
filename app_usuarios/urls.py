# urls app USUARIO
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('conta/', views.novo_usuario, name='novo_usuario'),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='usuarios/logout.html'), name='logout')
]