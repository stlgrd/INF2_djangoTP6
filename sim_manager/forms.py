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

# formulaire création utilisateur
class CreateProfileForm(forms.Form):
    username=forms.CharField(label="User's name:")
    email=forms.CharField(label="Email adress:")
    password=forms.CharField(label="Password:", widget=forms.PasswordInput())

#Formulaire modification mot de passe
class UpdatePasswordForm(forms.Form):
    password1 = forms.CharField(label="New password:", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Confirm password:", widget=forms.PasswordInput())

#Formulaire suppression compte
class DeleteAccountForm(forms.Form):
    choices = [('Yes', 'Yes'), ('No', 'No')]
    delete = forms.ChoiceField(label="Do you really want to delete your account ?", choices=choices, widget=forms.RadioSelect)