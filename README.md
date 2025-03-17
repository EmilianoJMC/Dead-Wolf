# 🎵 Music Streaming

Um aplicativo web para streaming de músicas, utilizando **Django** no backend, **Vue.js** no frontend e **MySQL** como banco de dados.

## 📂 Estrutura do Projeto

```
music_streaming/          # Diretório raiz do backend
│── manage.py             # Comando principal do Django
│── music_streaming/      # Configuração do projeto Django
│   │── settings.py       # Configurações Django
│   │── urls.py           # Rotas do Django
│   │── wsgi.py           # Configuração WSGI
│── music_app/            # Aplicação Django
│   │── models.py         # Modelos do banco de dados
│   │── views.py          # Lógica da API
│   │── serializers.py    # Serializadores para API REST
│   │── urls.py           # Rotas específicas da aplicação
│   │── admin.py          # Configuração do painel Django Admin
│── scripts/
│   │── load_musics.py    # Script para carregar músicas no banco
frontend/                 # Diretório do frontend Vue.js
│── src/
│   │── components/
│   │   │── HomePage.vue  # Página inicial
│   │   │── MusicAlbums.vue  # Lista de álbuns
│   │   │── MusicPlayer.vue  # Player de música
│── public/
│── package.json          # Dependências do Vue.js
│── vite.config.js        # Configuração do Vite
```

---

## 🚀 Instalação e Execução

### 📌 Backend (Django)

1. **Criar e ativar o ambiente virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```
2. **Instalar dependências**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configurar o banco de dados MySQL**
   - No arquivo `settings.py`, configurar:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'music_db',
           'USER': 'seu_usuario',
           'PASSWORD': 'sua_senha',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```
4. **Rodar migrações**
   ```bash
   python manage.py migrate
   ```
5. **Criar superusuário (opcional)**
   ```bash
   python manage.py createsuperuser
   ```
6. **Executar o servidor**
   ```bash
   python manage.py runserver
   ```

---

### 🎧 Carregar Músicas no Banco

1. Certifique-se de que as músicas estão organizadas assim:
   ```
   /caminho/para/musicas/
   ├── Disco1/
   │   ├── musica1.mp3
   │   ├── musica2.mp3
   ├── Disco2/
   │   ├── musica3.mp3
   │   ├── musica4.mp3
   ```
2. Execute o script para carregar as músicas no banco:
   ```bash
   python scripts/load_musics.py /caminho/para/musicas/
   ```

---

### 📌 Frontend (Vue.js)

1. **Instalar dependências**
   ```bash
   cd frontend
   npm install
   ```
2. **Executar o servidor**
   ```bash
   npm run dev
   ```

---

## 🔗 Endpoints da API

- `GET /api/discos/` → Retorna todos os discos.
- `GET /api/discos/{id}/` → Retorna um disco específico.
- `GET /api/musicas/` → Retorna todas as músicas.
- `GET /api/musicas/{id}/` → Retorna uma música específica.

---

## 🎵 Player de Música

O player de música no frontend permite:
- Selecionar um disco
- Listar todas as músicas do disco
- Reproduzir músicas diretamente no navegador

O **`MusicPlayer.vue`** faz uso da tag `<audio>` para reprodução.

```vue
<audio :src="musicaSelecionada.url" controls></audio>
```

---

## 📌 Possíveis Erros e Soluções

| Erro | Solução |
|------|---------|
| `django-admin: command not found` | Ative o ambiente virtual e instale as dependências. |
| `ModuleNotFoundError: No module named 'django.db'` | Certifique-se de que está dentro do ambiente virtual. |
| `mysqlclient.Error: Access denied for user` | Verifique o usuário e senha do MySQL em `settings.py`. |
| `npm: command not found` | Instale o Node.js e tente novamente. |

---

## 📜 Licença

Este projeto está licenciado sob a **MIT License**. Você pode modificá-lo e distribuí-lo livremente.

---

Desenvolvido por **Dead Wolf** 🎶

