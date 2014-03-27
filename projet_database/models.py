from django.db import models

# Create your models here.
class Cours (models.Model):
    Etablissement = models.CharField(max_length=20)
    Grade = models.CharField(choices=[('P','Propedeutique'),('L1','License 1'),('L2','License 2'),('L3','License 3'),('M1','Master 1'),('M2','Master 2')],max_length=5)
    Semestre = models.CharField(choices=[('S1','Semestre 1'),('S2','Semestre 2')],max_length=5)
    NomCours = models.CharField(max_length=20)

    def __unicode__(self):
        return u'%s-%s %s-%s' %(self.Etablissement, self.Grade, self.Semestre, self.NomCours)


class Programme (models.Model):
    Domaine = models.CharField(choices=[('E&G','Economie et Gestion'),('ST','Science et Technologie')],max_length=5)
    Mention =models.CharField(choices=[('SI','Science Informatique'),('E&G','Economie et Gestion')],max_length=5)
    Specialite = models.CharField(choices=[('SDE','Science de l\'Economie'),('SC','Science Comptable'),('BDD','Base de donnees'),('TEL','TELECOM'),('ONE','Organisation de la Net Economie'),('NOSP','No Speciality')],max_length=10)
    TypeCours = models.CharField(choices=[('OB','Obligatoire'),('OP','Optionnel')],max_length=5)
    Langue = models.CharField(choices=[('FR','Francais'),('AN','Anglais')],max_length=5)

    def __unicode__(self):
        return u'%s-%s-%s-%s-%s' %(self.Domaine, self.Mention, self.Specialite, self.TypeCours, self.Langue)


class Professeurs (models.Model):
    NomProf = models.CharField(max_length=20)
    PrenomProf = models.CharField(max_length=20)
    Tel = models.CharField(max_length=10)
    Sexe = models.CharField(choices=[('Homme','Homme'),('Femme','Femme')],max_length=6)
    CvProf = models.FileField(upload_to='CvProfs')
    Email = models.EmailField(max_length=50)

    def __unicode__(self):
        return u'%s %s %s %s %s' %(self.NomProf, self.PrenomProf, self.Tel, self.CvProf, self.Email)
   # Site = models.URLField()

class DescriptionCours (models.Model):
     CodeCours = models.ForeignKey(Cours)
     NomCours = models.CharField(max_length=20)
     CrediEcts = models.CharField(max_length=10)
     LieuEnseignement = models.CharField(max_length=20)
     #Etablissement = models.CharField(max_length=20)
     PublicCible = models.CharField(max_length=20)
     PreRequis = models.CharField(max_length=100)
     Objectif = models.CharField(max_length=100)
     Description = models.CharField(max_length=50)
     PlanCours = models.CharField(max_length=250)
     Format = models.CharField(max_length=50)
     Ressource = models.CharField(max_length=100)
     Evaluation = models.CharField(max_length=100)
     #cours = models.ForeignKey('Cours')

     def __unicode__(self):
         return u'%s %s %s %s %s %s %s %s %s %s %s' %(self.NomCours, self.CrediEcts, self.LieuEnseignemment, self.PublicCible, self.PreRequis, self.Objectif, self.Description, self.PlanCours, self.Format, self.Ressource, self.Evaluation)

