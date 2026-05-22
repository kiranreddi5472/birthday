from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WishViewSet, GalleryViewSet, DialogueViewSet, VoiceMessageView, random_message

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'wishes', WishViewSet, basename='wish')
router.register(r'gallery', GalleryViewSet, basename='gallery')
router.register(r'dialogues', DialogueViewSet, basename='dialogue')

urlpatterns = [
    # Router registered endpoints (/api/wishes/, /api/gallery/, /api/dialogues/)
    path('', include(router.urls)),
    
    # Custom endpoints
    path('voice-message/', VoiceMessageView.as_view(), name='voice-message'),
    path('random-message/', random_message, name='random-message'),
]
