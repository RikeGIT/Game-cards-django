# Web I - Estagio 2

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

Visite [http://localhost:8000](http://localhost:8000/) para ver a lista de jogos.

Você pode adicionar jogos pela rota http://localhost:8000/crud/jogo ou pela rota http://localhost:8000/admin
