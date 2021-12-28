"""djangoTP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.conf.urls.static import static
from sim_manager import views
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.landing),
    path('account/', include('django.contrib.auth.urls')),
    re_path(r'^profile/', views.edit_profile,name="profile"),
    re_path(r'^sim_list/', views.simulation_list,name="sim_list"),
    re_path(r'add_profile', views.add_profile, name="add_user"),  # ajouterprofil
    re_path(r'^modif_password', views.modif_password, name="modif_mdp"),  # url pour modifier le mdp
    re_path(r'^delete_account', views.delete_account, name="sup_user"),  # url pour supprimer le user
    re_path(r'^$', views.landing),
    re_path(r'^newsimu/$', views.new_simu, name='newsimu'),
    re_path(r'^(?P<object_id>[0-9]+)/run_sim/$', views.run_sim, name='run_sim'),
    re_path(r'^(?P<object_id>[0-9]+)/delete_sim/$', views.simulation_delete, name='delete_sim'),
    re_path(r'^(?P<object_id>[0-9]+)/mark_favorite_sim/$', views.mark_favorite_sim, name='mark_favorite_sim'),
    re_path(r'^(?P<object_id>[0-9]+)/share_sim/$', views.share_sim, name='share_sim'),
    re_path(r'^add_profile', views.edit_profile, name="add_user"),
]
