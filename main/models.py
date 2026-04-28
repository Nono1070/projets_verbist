from django.db import models
from django.contrib.auth.models import AbstractUser

# 1. Extension de l'utilisateur standard pour répondre aux critères du projet 
class User(AbstractUser):
    adresse = models.CharField(max_length=255, blank=True, null=True)
    code_postal = models.CharField(max_length=10, blank=True, null=True)
    date_naissance = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True) # [cite: 42]
    is_blocked = models.BooleanField(default=False) # Pour la gestion admin [cite: 66]

# 2. Modèle pour le Blog 
class Billet(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

class Commentaire(models.Model):
    billet = models.ForeignKey(Billet, on_delete=models.CASCADE, related_name='commentaires')
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    texte = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)

# 3. Modèle pour le Mini-Chat [cite: 29]
class ChatMessage(models.Model):
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255) # Longueur limitée [cite: 30]
    date_envoi = models.DateTimeField(auto_now_add=True)

# 4. Modèle pour la Boutique [cite: 46, 47]
class Article(models.Model):
    CATEGORIES = [
        ('INFO', 'Informatique'),
        ('LIVRE', 'Livre'),
        ('HIFI', 'Hi-Fi'),
    ]
    nom = models.CharField(max_length=100)
    categorie = models.CharField(max_length=10, choices=CATEGORIES)
    prix = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nom} ({self.categorie})"
