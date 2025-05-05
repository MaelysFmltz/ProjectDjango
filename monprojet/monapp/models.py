from django.db import models

# Create your models here.

class Pays(models.Model):
    nom = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

def __str__(self):
    return self.nom

class Region(models.Model):
    nom = models.CharField(max_length=100)
    superficie = models.IntegerField()
    population = models.IntegerField()
    capitale = models.CharField(max_length=100)
    pays= models.ForeignKey(Pays, on_delete=models.CASCADE,related_name='regions')

def __str__(self):
    return f"{self.nom} ({self.pays.nom})"

