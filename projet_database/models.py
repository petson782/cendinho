from django.db import models

# Create your models here.
class Cours (models.Model):
    Etablissement = models.CharField(max_length=20)
    Grade = models.CharField(max_length=5)
    Semestre = models.CharField(max_length=5)
    NomCours = models.CharField(max_length=20)


class Programme (models.Model):
    Domaine = models.CharField(max_length=5)
    Mention =models.CharField(max_length=5)
    Specialite = models.CharField(max_length=10)
    TypeCours = models.CharField(max_length=5)
    Langue = models.CharField(max_length=5)


class Professeurs (models.Model):
    NomProf = models.CharField(max_length=20)
    PrenomProf = models.CharField(max_length=20)
    Tel = models.CharField(max_length=10)
    CvProf = models.CharField(max_length=400)
    Email = models.EmailField(max_length=50)
    Site = models.URLField()

class DescriptionCours (models.Model):
     CodeCours = models.CharField(max_length=20)
     NomCours = models.CharField(max_length=20)
     CrediEcts = models.CharField(max_length=10)
     LieuEnseignement = models.CharField(max_length=20)
     Etablissement = models.CharField(max_length=20)
     CvProf = models.CharField(max_length=50)
     PublicCible = models.CharField(max_length=20)
     PreRequis = models.CharField(max_length=100)
     Objectif = models.CharField(max_length=100)
     Description = models.CharField(max_length=50)
     PlanCours = models.CharField(max_length=250)
     Format = models.CharField(max_length=50)
     Ressource = models.CharField(max_length=100)
     Evalution = models.CharField(max_length=100)
     cours = models.ForeignKey('Cours')