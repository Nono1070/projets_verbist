from django import forms
from .models import User

class InscriptionForm(forms.ModelForm):
    # Ajout du champ mot de passe avec masquage des caractères
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirmez le mot de passe")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'adresse', 'code_postal', 'date_naissance', 'avatar']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password") != cleaned_data.get("confirm_password"):
            raise forms.ValidationError("Les mots de passe ne correspondent pas.")
        return cleaned_data