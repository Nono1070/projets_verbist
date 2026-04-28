from django.shortcuts import render, redirect
from .forms import InscriptionForm
from django.contrib.auth import login

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
    return render(request, 'main/accueil.html')