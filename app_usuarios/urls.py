# urls app USUARIO
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

"""
Arquivo de configuração de URLs para o aplicativo de usuário.

Define os padrões de URL para a autenticação de usuário, incluindo
registro de novo usuário, login e logout.

Padrões:
- 'conta/': Rota para criar um novo usuário.
- 'login/': Rota para o processo de login usando a visualização incorporada do Django.
- 'logout/': Rota para o processo de logout usando a visualização incorporada do Django.
"""


urlpatterns = [
    path('conta/', views.novo_usuario, name='novo_usuario'),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='usuarios/logout.html'), name='logout')
]