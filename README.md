# Projeto_Rede_Social

<p align="justify">Este projeto implementa uma simples rede social usando o framework Django. Ele inclui funcionalidades como a criação de postagens, comentários, perfis de usuário, registro, login e logout.</p>

## 🗼 Principais Funcionalidades

### Postagens Dinâmicas

- Crie postagens facilmente usando o formulário intuitivo.
- Visualize postagens na página inicial, ordenadas pela data de publicação.

### Comentários Interativos

- Adicione comentários às postagens para iniciar conversas.
- Explore e interaja com comentários em cada postagem.

### Perfis de Usuário

- Visualize o perfil de outros usuários para conhecer suas postagens.
- Atualize e personalize seu próprio perfil.

### Registro e Autenticação

- Registre-se como novo usuário para ter acesso a todas as funcionalidades.
- Realize login e logout de forma segura.

### Gestão de Postagens

- Exclua suas próprias postagens.
- Edite o conteúdo das suas postagens.

## 🏗️ Estrutura do Projeto

O projeto é organizado em diferentes aplicativos:

- **app_rede_social:** Contém as funcionalidades principais da rede social, como postagens, comentários e perfis de usuário.
- **app_usuarios:** Gerencia o registro, login e logout de usuários.
- **rede_social** Pasta do projeto principal que gerencia as demais aplicações.

## 💻 Principais Componentes

### Modelos

- **Post:** Representa uma postagem na rede social.
- **Comentario:** Representa um comentário associado a uma postagem.
- **User:** Modelo padrão de usuário do Django, estendido para incluir o campo de e-mail.

### Formulários

- **PostForm:** Formulário para criar e editar postagens.
- **ComentarioForm:** Formulário para adicionar comentários a postagens.
- **UserRegisterForm:** Formulário de registro de usuário, estendendo o formulário padrão do Django.

### Views

- **lista_postagens:** Exibe a lista de postagens na página inicial.
- **detalhes_postagem:** Exibe os detalhes de uma postagem específica, incluindo comentários.
- **perfil_usuario:** Exibe o perfil do usuário, suas postagens e quantidade de comentários em cada postagem.
- **excluir_postagem:** Permite ao usuário excluir suas próprias postagens.
- **editar_postagem:** Permite ao usuário editar o conteúdo de suas postagens.
- **nova_postagem:** Permite ao usuário criar novas postagens.
- **visualizar_perfil:** Permite aos usuários visualizar o perfil de outros usuários.
- **novo_usuario:** Lida com o processo de registro de um novo usuário.

## 🔗 Configuração de URLs

O arquivo `urls.py` está configurado para rotear as solicitações para os aplicativos e suas respectivas views.

## 🛠️ Tecnologias Utilizadas

Principal tecnologia usada:</br>
**[Django](https://docs.djangoproject.com/en/4.2/)**</br>
**[Bootstrap5](https://getbootstrap.com/)**</br>

## Licença

Este projeto é licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter detalhes.

## 🚀 Instruções de Uso

### 👨‍💻 Crie um ambiente virtual

Para criar o ambiente virtual execute o seguinte código no terminal, substituindo o nome pelo seu nome ou outra palavra de sua preferência:

```bash
pip python -m venv nome
```

### 👨‍💻 Ative o ambiente vitual

Para ativar o ambiente virtual, execute o seguinte código no terminal, o nome aqui é mesmo que você definiu no passo anterior:

```bash
nome/scripts/activate
```

### 👨‍💻 Instalale as dependências

Para instalar as dependências do projeto, execute o seguinte comando no terminal:

```bash
pip install -r requirements.txt
```

### Execute as migrações e Crie um superusuário

Para fazer isso no terminal execute os seguintes comandos:

```bash
python manage.py migrate
```

```bash
python manage.py createsuperuser
```

### ✨ Execução do Programa

Execute o programa inserindo o seguinte comando no terminal, mas não esqueça de realizar os passos anteriores.

```bash
python manage.py runserver
```

O projeto estará acessível em [http://127.0.0.1:8000/](http://127.0.0.1:8000/). Acesse a interface administrativa em [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) para gerenciar usuários, postagens e comentários.

### 🚨 Observação

O site já está hospedado para quem quiser dá uma olha [🔗 Vizializar site!!](https://rede-social-qq1u.onrender.com). </br>
No entanto devido a hospedagem ser gratuita, o mesmo apresenta lentidão, além disso após um tempo inativo o site e pausado pela hospedagem, sendo necessário aguarda até 10min após a tentativa de acesso para que seja iniciado novamente.
