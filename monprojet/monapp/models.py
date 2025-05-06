from django.db import models

class Pays(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Region(models.Model):
    region = models.CharField(max_length=100)
    superficie = models.IntegerField()
    population = models.IntegerField()
    ville = models.CharField(max_length=100)
    pays = models.ForeignKey(Pays, on_delete=models.CASCADE, related_name='regions')

    def __str__(self):
        return self.region


