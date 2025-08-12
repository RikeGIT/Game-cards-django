# 🎮 Apresentação do Projeto

Olá!  
Este é o **GameCards**, uma rede de avaliação de jogos que nasceu como um projeto antigo e agora está evoluindo para um ambiente totalmente baseado em **Django**.

O objetivo é oferecer uma plataforma onde usuários possam cadastrar, avaliar e gerenciar informações sobre seus jogos favoritos, com um sistema robusto e organizado.  
Essa evolução trouxe melhorias importantes:

- 🔧 **Sistema CRUD de jogos** — Desenvolvido com *Class-Based Views* (CBVs) do Django, permitindo que administradores adicionem, editem e excluam jogos de forma dinâmica.
- 🔐 **Sistema de login e registro** — Usuários podem criar contas para personalizar suas avaliações.
- 🗄 **Banco de dados relacional com MySQL** — Estrutura migrada para um banco relacional, garantindo melhor desempenho e organização dos dados.

Ainda há muito a ser aprimorado, mas esta é apenas a primeira etapa dessa jornada. 🚀

📌 Confira a publicação completa no LinkedIn:  
[🔗 Post sobre o GameCards](https://www.linkedin.com/feed/update/urn:li:activity:7328492332767408128/)


**🚀 Como usar**

**1. Crie um ambiente virtual**

```
python -m venv venv
```

**2. Inicie o ambiente virtual**

```
venv\Scripts\activate
```

**3. Instale as dependências**

```
pip install -r requirements.txt
```

**4. Configure seu banco MYSQL no `settings.py`**

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gamecards',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

**5. Crie o seu banco no Mysql Workbench**

```
CREATE DATABASE gameCards CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;jogos_jogo
```

**6. Execute migrações**

```
python manage.py makemigrations
python manage.py migrate
```

**7. Rode o servidor de desenvolvimento**

```
python manage.py runserver
```

**8. Acesse a aplicação**

Visite [http://localhost:8000](http://localhost:8000/) para ver a pagina principal

**9. Segurança e como utilizar o crud**

Para acessar o CRUD, você deve estar logado como um **administrador do Django**. Crie um superusuário com:

```
python manage.py createsuperuser
```

Em seguida, você poderá adicionar jogos acessando:

http://localhost:8000/crud/jogo

Caso não esteja logado, será redirecionado para a página de login ou receberá um **erro 403**.
