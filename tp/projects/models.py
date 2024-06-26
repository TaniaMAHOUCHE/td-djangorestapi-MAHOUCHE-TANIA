from django.db import models

# Create your models here.

class Chercheur(models.Model):
    nom = models.CharField(max_length=100)
    specialite = models.CharField(max_length=100, default='specialite')
    projets = models.ManyToManyField('ProjetDeRecherche', blank=True)
    # projets = models.ManyToManyField('ProjetDeRecherche', related_name='chercheurs_associes', blank=True)

class ProjetDeRecherche(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin_prevue = models.DateField(blank=True, null=True)
    # chef_de_projet = models.ForeignKey(Chercheur, related_name='projets_recherches', related_query_name='projet', on_delete=models.CASCADE)
    chef_de_projet = models.ForeignKey(Chercheur, related_name='projets_recherches', related_query_name='projet', on_delete=models.CASCADE, blank=True, null=True)

class Publication(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_publication = models.DateField()
    auteur = models.ForeignKey(Chercheur, related_name='publications', related_query_name='publication', on_delete=models.CASCADE)

