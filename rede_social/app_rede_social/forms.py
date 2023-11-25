from django.forms import ModelForm
from .models import Post, Comentario

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = ('texto',)