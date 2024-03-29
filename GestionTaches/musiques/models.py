from django.db import models
from django.urls import reverse


class Artiste(models.Model):
    nom = models.CharField(max_length=64)
    def __str__(self):
        return '{self.nom}'.format(self=self)
    def get_absolute_url(self):
        return reverse('musiques:artiste-detail', kwargs={'pk': self.pk})

class Morceau(models.Model):
    titre = models.CharField(max_length=64)
    artiste = models.CharField(max_length=64)
    date_sortie = models.DateField(null=True)
    interprete = models.ForeignKey(Artiste, on_delete=models.CASCADE, related_name="morceaux", null=True)

    def __str__(self):
        return '{self.titre} ({self.artiste})'.format(self=self)
    def get_absolute_url(self):
        return reverse('musiques:morceau-detail', kwargs={'pk': self.pk})

