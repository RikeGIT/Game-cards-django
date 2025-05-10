# Web I - Estagio 2

**🚀 Como usar**

**1. Instale as dependências**

```
pip install -r requirements.txt
```

**2. Configure seu banco MYSQL no `settings.py`**

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

**3. Crie o seu banco no Mysql Workbench**

```
CREATE DATABASE gameCards CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;jogos_jogo
```

**4. Execute migrações**

```
python manage.py makemigrations
python manage.py migrate
```

**5. Carregue os dados no Projeto**

```
python manage.py loaddata dados.json
```

**6. Rode o servidor de desenvolvimento**

```
python manage.py runserver
```

**7. Acesse a aplicação**

Visite [http://localhost:8000](http://localhost:8000/) para ver a lista de jogos.

Você pode adicionar jogos pela rota crud/jogo ou pelo admin
