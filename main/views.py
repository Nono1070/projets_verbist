from django.shortcuts import render, redirect
from .forms import InscriptionForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST, request.FILES) # request.FILES pour l'image/avatar [cite: 42]
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password']) # Cryptage du mot de passe 
            user.save()
            login(request, user) # Connecte l'utilisateur après inscription
            return redirect('accueil')
    else:
        form = InscriptionForm()
    return render(request, 'main/inscription.html', {'form': form})

def accueil(request):
    # Si l'utilisateur remplit le formulaire de connexion sur l'accueil
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('accueil')
    else:
        form = AuthenticationForm()
    
    return render(request, 'main/accueil.html', {'form': form})
@login_required # Seul un membre connecté peut voir cette page
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