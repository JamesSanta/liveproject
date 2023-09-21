from . import views
from django.urls import path, include
from .views import CharacterView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('sw_home', views.sw_home, name='sw_home'),
    path('add_character', views.add_character, name='add_character'),
    path('character_view', CharacterView.as_view(), name='characters'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
