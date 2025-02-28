from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlbumViewSet, MusicViewSet, home, react_app

router = DefaultRouter()
router.register(r'albums', AlbumViewSet)
router.register(r'musics', MusicViewSet)

urlpatterns = [
    path('home/', home, name='home'),  # Página inicial do Django
    path('api/', include(router.urls)),
    path('', react_app, name='react_app'),  # React servido pelo Django
]
