from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post, Comentario
from .forms import PostForm, ComentarioForm


def lista_postagens(request):
    postagens = Post.objects.all().order_by("-data_publicacao")
    return render(request, "paginas/home.html", {"postagens": postagens})


@login_required
def perfil_usuario(request, user):
    user_ = User.objects.get(username=user)
    if user_.username == str(request.user):
        postagens = Post.objects.filter(user=user_.id).order_by("-data_publicacao")
        lista_quant_comen = [len(Comentario.objects.filter(post=postagem)) for postagem in postagens]
        if len(postagens) > 0:
            return render(request, "paginas/perfil_usuario.html", {"postagens": zip(postagens,lista_quant_comen)})
    return render(request, "paginas/perfil_usuario.html")
    

@login_required
def visualizar_perfil(request, user):
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
    postagem = Post.objects.get(id=id_postagem)
    if request.method == "POST":
        if request.user == postagem.user:
            postagem.delete()
        return redirect("perfil_usuario", request.user)

    return render(request, "paginas/excluir_postagem.html", {"postagem": postagem})


@login_required
def editar_postagem(request, id_postagem):
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
    if request.method == "POST":
        user_id = User.objects.get(username=request.user)
        texto = request.POST["publicacao"]
        if texto.strip():
            nova_publicacao = Post(user=user_id, texto=texto)
            nova_publicacao.save()
            return redirect('perfil_usuario', request.user)
    return render(request, "paginas/nova_publicacao.html")
