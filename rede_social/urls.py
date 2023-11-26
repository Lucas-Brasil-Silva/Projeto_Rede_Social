from django.contrib import admin
from django.urls import path, include

"""
Configuração de URLs para o projeto da Rede Social.

Padrões:
- 'admin/': Rota para a interface administrativa do Django.
- '': Inclui as URLs do aplicativo principal ('app_rede_social.urls').
- 'usuario/': Inclui as URLs do aplicativo de usuários ('app_usuarios.urls').
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_rede_social.urls')),
    path('usuario/', include('app_usuarios.urls'))
]