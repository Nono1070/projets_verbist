from django.contrib import admin
from .models import Article, Commentaire, ChatMessage, User

# On enregistre tes modèles pour qu'ils apparaissent dans l'admin
admin.site.register(Article)
admin.site.register(Commentaire)
admin.site.register(ChatMessage)
admin.site.register(User)