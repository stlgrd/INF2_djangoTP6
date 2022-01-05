from django import forms
from .models import Simulation, Share
from django.contrib.auth.models import User


class SimuForm(forms.ModelForm):
    class Meta:
        model = Simulation
        fields = '__all__'


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

# ajout :

class ShareForm(forms.ModelForm):
    class Meta:
        model = Share
        fields = '__all__'

#Formulaire pour créer un utilisateur
class CreateProfileForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    email = forms.CharField(label="Adresse email", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput())

#Formulaire pour modifier le mot de passe
class UpdatePasswordForm(forms.Form):
    password1 = forms.CharField(label="Nouveau mot de passe", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Confirmer le mot de passe", widget=forms.PasswordInput())

#Formulaire suppression compte
class DeleteAccountForm(forms.Form):
    choices = [('Yes', 'Yes'), ('No', 'No')]
    delete = forms.ChoiceField(label="Do you really want to delete your account ?", choices=choices, widget=forms.RadioSelect)