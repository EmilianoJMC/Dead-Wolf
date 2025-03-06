from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse

def home(request):
    return HttpResponse("Página Inicial do Streaming de Músicas")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('music_app.urls')),
    path('', home),  # Adiciona a rota para a página inicial
]