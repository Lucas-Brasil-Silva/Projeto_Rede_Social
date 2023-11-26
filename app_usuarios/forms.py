from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    """
    Formulário de registro de usuário personalizado.

    Este formulário estende o formulário padrão de criação de usuário do Django
    (UserCreationForm) e adiciona um campo de e-mail.

    Model:
    - User: Modelo de usuário padrão do Django.

    Fields:
    - 'username': Campo para inserção do nome de usuário.
    - 'email': Campo para inserção do endereço de e-mail.
    - 'password1': Campo para inserção da senha.
    - 'password2': Campo para confirmação da senha.

    Adicionais:
    - 'email': Campo extra para inserção do endereço de e-mail.
    """
    
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']