from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post, Comentario
from .forms import PostForm, ComentarioForm


def lista_postagens(request):
    """
    Lista todas as postagens ordenadas por data de publicação.

    Parameters:
    - request: HttpRequest object.

    Returns:
    - HttpResponse object.
    """

    postagens = Post.objects.all().order_by("-data_publicacao")
    return render(request, "paginas/home.html", {"postagens": postagens})


@login_required
def perfil_usuario(request, user):
    """
    Exibe o perfil do usuário, incluindo suas postagens.

    Parameters:
    - request: HttpRequest object.
    - user: Username do usuário.

    Returns:
    - HttpResponse object.
    """

    user_ = User.objects.get(username=user)
    if user_.username == str(request.user):
        postagens = Post.objects.filter(user=user_.id).order_by("-data_publicacao")
        # Lista a quantidade de comentários para cada postagem.
        lista_quant_comen = [len(Comentario.objects.filter(post=postagem)) for postagem in postagens]
        if len(postagens) > 0:
            return render(request, "paginas/perfil_usuario.html", {"postagens": zip(postagens,lista_quant_comen)})
    return render(request, "paginas/perfil_usuario.html")
    

@login_required
def visualizar_perfil(request, user):
    """
    Esta função é usada para exibir o perfil de um usuário específico, incluindo suas postagens e a quantidade de comentários em cada postagem. Se o usuário logado for o mesmo que está sendo visualizado, ele será redirecionado para a própria página de perfil.

    Parameters:
    - request: HttpRequest object.
    - user: Username do usuário.

    Returns:
    - HttpResponse object.
    """

    if not str(request.user) == user:
        user_ = User.objects.get(username=user)
        postagens = Post.objects.filter(user=user_.id).order_by("-data_publicacao")
        lista_quant_comen = [len(Comentario.objects.filter(post=postagem)) for postagem in postagens]
        if len(postagens) > 0:
            return render(request, "paginas/visualizar_perfil.html", {"postagens": zip(postagens,lista_quant_comen),"perfil":user})
        return render(request, "paginas/visualizar_perfil.html")
    else:
        return redirect('perfil_usuario', user)

@login_required
def detalhes_postagem(request, id_postagem):
    """
    Essa função exibe os detalhes de uma postagem específica, incluindo o texto da postagem, os comentários associados a ela e os usuários que fizeram esses comentários. Os usuários podem adicionar novos comentários à postagem.

    Parameters:
    - request: HttpRequest object.
    - id_postagem: Id da postagem.

    Returns:
    - HttpResponse object.
    """

    if request.method == "POST":
        post = Post.objects.get(id=id_postagem).id
        user_id = User.objects.get(username=request.user)
        texto = request.POST["comentario"]
        if texto.strip():
            novo_comentario = Comentario(post_id=post, User=user_id, texto=texto)
            novo_comentario.save()
        return redirect('detalhes_postagem', id_postagem)
    postagem = Post.objects.get(id=id_postagem)
    comentario = Comentario.objects.filter(post_id=id_postagem).order_by("-data_comentario")
    user_name = [User.objects.get(id=dado.User_id) for dado in comentario]

    return render(
        request,
        "paginas/detalhes_postagem.html",
        {"postagem": postagem, "comentarios_users": zip(comentario, user_name),"quantidade":len(comentario)},
    )


@login_required
def excluir_postagem(request, id_postagem):
    """
    A função é usada para excluir uma postagem específica. Se o usuário logado for o autor da postagem, a postagem será excluída e o usuário será redirecionado para a sua própria página de perfil.

    Parameters:
    - request: HttpRequest object.
    - id_postagem: Id da postagem.

    Returns:
    - HttpResponse object.
    """

    postagem = Post.objects.get(id=id_postagem)
    if request.method == "POST":
        if request.user == postagem.user:
            postagem.delete()
        return redirect("perfil_usuario", request.user)

    return render(request, "paginas/excluir_postagem.html", {"postagem": postagem})


@login_required
def editar_postagem(request, id_postagem):
    """
    Esta função permite que o autor de uma postagem edite o texto da postagem. Se o usuário logado for o autor da postagem, o texto da postagem será atualizado com o novo texto fornecido.

    Parameters:
    - request: HttpRequest object.
    - id_postagem: Id da postagem.

    Returns:
    - HttpResponse object.
    """

    postagem = Post.objects.get(id=id_postagem)
    if request.method == "POST":
        if request.user == postagem.user:
            texto = request.POST["publicacao"]
            if texto.strip():
                postagem.texto = texto
                postagem.save()
        return redirect("perfil_usuario", request.user)
    publicacao = postagem.texto
    return render(request,"paginas/editar_postagem.html",{"publicacao": postagem.texto})


@login_required
def nova_postagem(request):
    """
    A função é responsável por permitir que os usuários criem novas postagens. Se um formulário de nova postagem for enviado por meio de uma solicitação POST válida, uma nova postagem será criada e associada ao usuário logado.

    Parameters:
    - request: HttpRequest object.

    Returns:
    - HttpResponse object.
    """

    if request.method == "POST":
        user_id = User.objects.get(username=request.user)
        texto = request.POST["publicacao"]
        if texto.strip():
            nova_publicacao = Post(user=user_id, texto=texto)
            nova_publicacao.save()
            return redirect('perfil_usuario', request.user)
    return render(request, "paginas/nova_publicacao.html")
