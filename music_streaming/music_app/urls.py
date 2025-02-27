from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlbumViewSet, MusicViewSet

router = DefaultRouter()
router.register(r'albums', AlbumViewSet)
router.register(r'musics', MusicViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
