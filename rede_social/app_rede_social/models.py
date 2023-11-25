from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)


class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    data_comentario = models.DateTimeField(auto_now_add=True)
