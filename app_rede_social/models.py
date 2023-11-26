from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Post(models.Model):
    """
    Representa uma postagem no sistema.

    Fields:
    - user: Usuário que fez a postagem.
    - texto: Texto da postagem.
    - data_publicacao: Data de publicação da postagem.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)


class Comentario(models.Model):
    """
    Representa um comentário em uma postagem.

    Fields:
    - post: Postagem à qual o comentário está associado.
    - user: Usuário que fez o comentário.
    - texto: Texto do comentário.
    - data_comentario: Data de publicação do comentário.
    """
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    data_comentario = models.DateTimeField(auto_now_add=True)
