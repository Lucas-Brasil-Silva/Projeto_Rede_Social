from django.forms import ModelForm
from .models import Post, Comentario

class PostForm(ModelForm):
    """
    Formulário para criar e editar postagens.

    Este formulário é baseado no modelo Post e inclui todos os campos disponíveis.

    Model:
    - Post: Modelo de postagem.

    Fields:
    - Todos os campos do modelo Post.
    """

    class Meta:
        model = Post
        fields = '__all__'

class ComentarioForm(ModelForm):
    """
    Formulário para adicionar comentários a postagens.

    Este formulário é baseado no modelo Comentario e inclui o campo 'texto' para o conteúdo do comentário.

    Model:
    - Comentario: Modelo de comentário associado a uma postagem.

    Fields:
    - 'texto': Campo para inserção do conteúdo do comentário.
    """
    
    class Meta:
        model = Comentario
        fields = ('texto',)