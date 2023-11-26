from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def novo_usuario(request):
    """
    View para criar um novo usuário no sistema.

    Exibe um formulário de registro e processa os dados submetidos via método POST.
    Se o formulário for válido, cria um novo usuário, exibe uma mensagem de sucesso
    e redireciona o usuário para a página de login.

    Parameters:
    - request: HttpRequest object.

    Returns:
    - HttpResponse object.
    """
    
    formulario = UserRegisterForm()
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            messages.success(request,f'O usuário {usuario} foi criado com sucesso!')
            formulario.save()
            return redirect('login')
    return render(request, 'usuarios/registrar.html', {'formulario':formulario})