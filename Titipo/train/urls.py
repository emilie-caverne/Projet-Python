from django.urls import path

from . import views

urlpatterns = [
    path("", views.acceuil, name="acceuil"),
    path("details/<id_train>", views.details, name="details"),
    path("aleatoire", views.aleatoire, name="aleatoire"),
]
