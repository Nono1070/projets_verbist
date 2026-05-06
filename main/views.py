from django.shortcuts import render, redirect, get_object_or_404  # <--- AJOUTÉ ICI
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# Import de tes modèles et formulaires
from .models import ChatMessage, Article, Commentaire
from .forms import InscriptionForm, ModifierProfilForm

# 1. ACCUEIL
def accueil(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('accueil')
    else:
        form = AuthenticationForm()
    return render(request, 'main/accueil.html', {'form': form})

# 2. INSCRIPTION
def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password']) 
            user.save()
            login(request, user)
            return redirect('accueil')
    else:
        form = InscriptionForm()
    return render(request, 'main/inscription.html', {'form': form})

# 3. PROFIL
@login_required
def profil(request):
    if request.method == 'POST':
        form = ModifierProfilForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profil mis à jour !")
            return redirect('profil')
    else:
        form = ModifierProfilForm(instance=request.user)
    return render(request, 'main/profil.html', {'form': form})

# 4. MINI-CHAT
@login_required
def mini_chat(request):
    if request.method == 'POST':
        texte = request.POST.get('message')
        if texte:
            ChatMessage.objects.create(auteur=request.user, message=texte[:255])
            return redirect('mini_chat')

    messages_chat = ChatMessage.objects.all().order_by('-date_envoi')[:10]
    return render(request, 'main/mini_chat.html', {'messages_chat': messages_chat})

# 5. CONNEXION
def connexion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('accueil')
    else:
        form = AuthenticationForm()
    return render(request, 'main/connexion.html', {'form': form})

# 6. DECONNEXION
def deconnexion(request):
    logout(request)
    return redirect('accueil')

# 7. BLOG (Liste)
def liste_articles(request):
    query = request.GET.get('search')
    if query:
        articles = Article.objects.filter(titre__icontains=query).order_by('-date_publication')
    else:
        articles = Article.objects.all().order_by('-date_publication')
    return render(request, 'main/blog.html', {'articles': articles, 'query': query})

# 8. DETAIL ARTICLE & COMMENTAIRES
def detail_article(request, article_id):
    article = get_object_or_404(Article, id=article_id) # <--- Utilise maintenant l'import ajouté
    commentaires = Commentaire.objects.filter(article=article).order_by('-date_publication')

    if request.method == 'POST' and request.user.is_authenticated:
        contenu = request.POST.get('contenu')
        if contenu:
            Commentaire.objects.create(
                article=article,
                auteur=request.user,
                contenu=contenu
            )
            return redirect('detail_article', article_id=article.id)

    return render(request, 'main/article_detail.html', {
        'article': article,
        'commentaires': commentaires
    })