from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import AlbumViewSet, MusicViewSet

router = DefaultRouter()
router.register(r'albums', AlbumViewSet)
router.register(r'musics', MusicViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
