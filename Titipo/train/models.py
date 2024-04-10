from django.db import models

# Create your models here.
class Train(models.Model) :
    trainID = models.AutoField(primary_key=True)
    depart = models.CharField(max_length = 50)
    arrivee = models.CharField(max_length = 50)
    heureDepart = models.CharField(max_length = 6)
    heureArrivee = models.CharField(max_length = 6)
    dureeTrajet = models.CharField(max_length = 6)
    info = models.CharField(max_length = 4000)
    image = models.ImageField(upload_to='static/IMG/', blank=True, null=True)
    prix = models.CharField(max_length=10)
