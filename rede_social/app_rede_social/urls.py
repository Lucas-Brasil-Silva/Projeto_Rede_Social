# urls app
from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_postagens, name="home"),
    path("post/<int:id_postagem>/", views.detalhes_postagem, name="detalhes_postagem"),
    path("perfil/usuario/<str:user>/", views.perfil_usuario, name="perfil_usuario"),
    path("excluir/<int:id_postagem>/", views.excluir_postagem, name="excluir_postagem"),
    path("editar/<int:id_postagem>/", views.editar_postagem, name="editar_postagem"),
    path("nova_publicacao/", views.nova_postagem, name="nova_publicacao"),
    path("visualizar/perfil/<str:user>/", views.visualizar_perfil, name="visualizar_perfil"),
]
