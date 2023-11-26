# urls app
from django.urls import path
from . import views

"""
Arquivo de configuração de URLs para o aplicativo principal.

Define os padrões de URL para as funcionalidades principais do aplicativo,
incluindo listagem de postagens, detalhes de postagem, perfil de usuário,
exclusão e edição de postagens, criação de novas publicações e visualização
do perfil de outros usuários.

Padrões:
- '': Rota padrão, exibe a lista de postagens na página inicial.
- 'post/<int:id_postagem>/': Rota para visualizar os detalhes de uma postagem específica.
- 'perfil/usuario/<str:user>/': Rota para visualizar o perfil de um usuário, incluindo suas postagens.
- 'excluir/<int:id_postagem>/': Rota para excluir uma postagem específica.
- 'editar/<int:id_postagem>/': Rota para editar o conteúdo de uma postagem.
- 'nova_publicacao/': Rota para criar uma nova postagem.
- 'visualizar/perfil/<str:user>/': Rota para visualizar o perfil de outro usuário.
"""

urlpatterns = [
    path("", views.lista_postagens, name="home"),
    path("post/<int:id_postagem>/", views.detalhes_postagem, name="detalhes_postagem"),
    path("perfil/usuario/<str:user>/", views.perfil_usuario, name="perfil_usuario"),
    path("excluir/<int:id_postagem>/", views.excluir_postagem, name="excluir_postagem"),
    path("editar/<int:id_postagem>/", views.editar_postagem, name="editar_postagem"),
    path("nova_publicacao/", views.nova_postagem, name="nova_publicacao"),
    path("visualizar/perfil/<str:user>/", views.visualizar_perfil, name="visualizar_perfil"),
]
