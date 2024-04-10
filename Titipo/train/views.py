from django.shortcuts import render
from train.models import Train
import random


# Create your views here.

def acceuil(request) :
    if 'q' in request.GET:
        query = request.GET['q']
        trains = Train.objects.filter(arrivee__icontains=query)
    else:
        trains = Train.objects.all()

    return render(request, "acceuil.html", {
        "trains": trains,
    })

def details(request, id_train) :
    myTrains = Train.objects.get(trainID = id_train)

    return render(request, "details.html", {
        "depart" : myTrains.depart,
        "arrivee" : myTrains.arrivee,
        "heureDepart" : myTrains.heureDepart,
        "heureArrivee" : myTrains.heureArrivee,
        "dureeTrajet" : myTrains.dureeTrajet,
        "info" : myTrains.info,
        "prix" : myTrains.prix,
        "image" : myTrains.image,
        "precedent" : int(id_train) - 1,
        "suivant" : int(id_train) + 1,
    })

def aleatoire(request):
    trains = random.choice(Train.objects.all())
    return render(request, 'aleatoire.html', {'trains': trains})