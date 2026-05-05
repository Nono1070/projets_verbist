from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main import views

urlpatterns = [
    # Administration
    path('admin/', admin.site.urls), 
    
    # Accueil et Inscription
    path('', views.accueil, name='accueil'),
    path('inscription/', views.inscription, name='inscription'),
    
    # Authentification
    path('connexion/', views.connexion, name='connexion'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    
    # Profil Membre (UM)
    path('profil/', views.profil, name='profil'),

    # Mini-Chat (uniquement pour UM)
    path('chat/', views.mini_chat, name='mini_chat'),
]

# Indispensable pour afficher les images/avatars
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)