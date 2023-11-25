from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def novo_usuario(request):
    formulario = UserRegisterForm()
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            messages.success(request,f'O usuário {usuario} foi criado com sucesso!')
            formulario.save()
            return redirect('login')
    return render(request, 'usuarios/registrar.html', {'formulario':formulario})

# paulo
#p@ulo1234
# paulo2
#p@ulo1234