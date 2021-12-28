from django.shortcuts import render, get_object_or_404, redirect
from django.forms.models import model_to_dict
from .models import Simulation, Share
from .forms import UserProfileForm, SimuForm, CreateProfileForm, UpdatePasswordForm, DeleteAccountForm, ShareForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from pyfhn.fhn_runner import run_fhn_base
import matplotlib.pyplot as plt
from io import StringIO
from django.contrib.auth import authenticate, login

# Create your views here.
def landing(request):
    return render(request, "base.html", locals())

@login_required(login_url="/account/login/")
def simulation_list(request):
    simulations = Simulation.objects.filter(user=request.user).order_by('is_favorite').reverse()
    shares=Share.objects.filter(user_shared=request.user)
    simulations_shares=shares.Simulation_set.all()
    return render(request, "simulation_list.html", {"user_sims": simulations, })

@login_required(login_url="/account/login/")
def edit_profile(request):
    if request.method == "POST":
        user_profile_form = UserProfileForm(request.POST)
        if user_profile_form.is_valid() and user_profile_form.cleaned_data["email"]:
            current_user = User.objects.get(username=request.user.username)
            current_user.first_name = user_profile_form.cleaned_data["first_name"]
            current_user.last_name = user_profile_form.cleaned_data["last_name"]
            current_user.email = user_profile_form.cleaned_data["email"]
            current_user.save()
    else:
        user_profile_form = UserProfileForm(instance=request.user)
    return render(request, "edit_profile.html", {"form": user_profile_form})

@login_required(login_url="/account/login/")
def new_simu(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = SimuForm(request.POST, request.FILES)
    if form.is_valid():

        params = form.cleaned_data
        print(params)
        newsim = Simulation(
            user=params["user"],
            alpha=params["alpha"],
            beta=params["beta"],
            gamma=params["gamma"],
            delta=params["delta"],
            epsilon=params["epsilon"],
            is_favorite=params["is_favorite"],
        )
        newsim.save()
        return run_sim(request, newsim.id)
    return render(request, "newsimu.html", locals())

def run_sim(request, object_id):
    params = model_to_dict(get_object_or_404(Simulation, pk=object_id), exclude=['is_favorite', 'is_shared', 'user_shared'])
    params.pop("user")
    params.pop("id")
    res = run_fhn_base(params)
    f = plt.figure()
    plt.title("FHN Simulation")
    plt.xlabel("Time")
    plt.ylabel("Outputs")
    plot = plt.plot(res["t"], res["y"][0], res["t"], res["y"][1])
    plt.legend(["v", "w"])
    imgdata = StringIO()
    f.savefig(imgdata, format="svg")
    imgdata.seek(0)

    data = imgdata.getvalue()
    return render(request, "graphic.html", {"graphic": data})

@login_required(login_url="/login/")
def simulation_delete(request, object_id):
    sim = get_object_or_404(Simulation, pk=object_id)
    sim.delete()
    return HttpResponseRedirect(reverse_lazy("sim_list"))

# ajout :

def add_profile(request):
    "Créer un nouvel utilisateur"
    if request.method == "POST":
        profile_create_form = CreateProfileForm(request.POST)
        #Si le formulaire envoyé est valide
        if profile_create_form.is_valid() and profile_create_form.cleaned_data["email"]:
            #Récupération des informations
            username = profile_create_form.cleaned_data["username"]
            password = profile_create_form.cleaned_data["password"]
            email = profile_create_form.cleaned_data["email"]
            #On regarde si un utilisateur avec cet username existe déjà
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                #Impossible de créer l'utlisateur
                pass
            else:
                #Création de l'utilisateur
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                #Connecte automatiquement l'utilisateur après son inscription
                user = authenticate(request, username=username, password=password)
                login(request, user)
                return redirect("add_profile.html")
    else:
        profile_create_form = CreateProfileForm()
    return render(request, "add_profile.html", {"form": profile_create_form})


@login_required(login_url="/account/login/")
def modif_password(request):
    "Modifier le mot de passe de l'utilisateur"
    if request.method == "POST":
        update_password_form = UpdatePasswordForm(request.POST)
        # Si le formulaire envoyé est valide
        if update_password_form.is_valid():
            #Récupération des mots de passe saisis
            password1 = update_password_form.cleaned_data["password1"]
            password2 = update_password_form.cleaned_data["password2"]
            #Si l'utilisateur a saisi 2 fois le même mot de passe, on peut effectuer la modification
            if password1 == password2:
                #Récupère le compte de l'utilisateur
                user = User.objects.get(username=request.user.username)
                #Modification du mot de passe
                user.set_password(password1)
                #Sauvegarde des modifications
                user.save()
            else:
                pass
    else:
        update_password_form = UpdatePasswordForm()
    return render(request, "modif_password.html", {"form": update_password_form})

@login_required(login_url="/account/login/")
def delete_account(request):
    "Supprimer le compte de l'utilisateur"
    envoi = False
    if request.method == "POST":
        envoi = True
        delete_account_form = DeleteAccountForm(request.POST)
        # Si le formulaire envoyé est valide
        if delete_account_form.is_valid():
            # Récupération du choix de l'utilisateur
            choice = delete_account_form.cleaned_data['delete']
            # Si l'utilisateur a choisi de supprimer son compte
            if choice == 'Yes':
                supprime = True
                # Récupère le compte de l'utilisateur
                user = User.objects.get(username=request.user.username)
                # Suppression de l'utilisateur
                user.delete()
            else:
                #Sinon, on ne supprime pas le compte
                supprime = False
    else:
        delete_account_form = DeleteAccountForm()
    return render(request, "delete_account.html", {"form": delete_account_form})

@login_required(login_url="/account/login/")
def mark_favorite_sim(request, object_id):
    sim = get_object_or_404(Simulation, pk=object_id)
    sim.is_favorite = not sim.is_favorite
    sim.save()
    print(sim.is_favorite)
    return HttpResponseRedirect(reverse_lazy("sim_list"))

@login_required(login_url="/account/login/")
def share_sim(request):
    print('Coucou')
    users_form = ShareForm(request.POST)
    return render(request, "share_sim.html", {"form": users_form})

# @login_required(login_url="/account/login/")
# def edit_profile(request):
#     if request.method == "POST":
#         user_profile_form = SimuForm(request.POST)
#         if user_profile_form.is_valid() and user_profile_form.cleaned_data["email"]:
#             current_user = User.objects.get(username=request.user.username)
#             current_user.first_name = user_profile_form.cleaned_data["first_name"]
#             current_user.last_name = user_profile_form.cleaned_data["last_name"]
#             current_user.email = user_profile_form.cleaned_data["email"]
#             current_user.save()
#     else:
#         user_profile_form = UserProfileForm(instance=request.user)
#     return render(request, "edit_profile.html", {"form": user_profile_form})