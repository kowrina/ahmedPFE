from django.db import models



class Classe(models.Model):
    filier = models.ForeignKey('Filier', on_delete=models.CASCADE)
    niveau = models.ForeignKey('Niveau',on_delete=models.CASCADE)
    nom = models.CharField(max_length=100, blank=False , default=None, null=False)

    matier_etu = models.ManyToManyField('Matier')


    def __str__(self):
        return self.nom
    class Meta:
        verbose_name_plural = "classe"


class Creneau(models.Model):
    numero = models.IntegerField(blank=False , default=None, null=False)
    nom = models.CharField(max_length=100, blank=False , default=None, null=False)
    debut = models.TimeField(max_length=100, blank=False , default=None, null=False)
    fin = models.TimeField(max_length=100, blank=False , default=None, null=False)

    def __str__(self):
        return self.nom
    class Meta:
        verbose_name_plural = "Créneau"



class Cours(models.Model):
    nom = models.CharField(max_length=100, blank=False , default=None, null=False)
    groupe = models.ForeignKey('Groupe', on_delete=models.CASCADE,blank=False , default=None, null=False)
    matier = models.ForeignKey('Matier', on_delete=models.CASCADE,blank=False , default=None, null=False)
    prof = models.ForeignKey('Professeur', on_delete=models.CASCADE,blank=False , default=None, null=False)
    salle = models.ForeignKey('Salle', on_delete=models.CASCADE ,blank=False , default=None, null=False)
    charge = models.IntegerField(blank=False , default=None, null=False)


    def __str__(self):
        return self.nom
    class Meta:
        #unique_together = (('groupe','matier','prof','salle'))
        verbose_name_plural = "cours"

class Departement(models.Model):
    nom = models.CharField(max_length=100, blank=False , default=None, null=False)
    chef = models.CharField(max_length=100, blank=False , default=None, null=False)
    email = models.EmailField(max_length=100, blank=False , default=None, null=False)
    mobile = models.CharField(max_length=100, blank=False , null=False)

    def __str__(self):
        return self.nom
    class Meta:
        verbose_name_plural = "departement"




class Filier(models.Model):
    dep = models.ForeignKey(Departement,on_delete=models.CASCADE)
    nom = models.CharField(max_length=100, blank=False , default=None, null=False)

    def __str__(self):
        return self.nom
    class Meta:
        verbose_name_plural = "filiére"

class Groupe(models.Model):
    classe = models.ForeignKey(Classe,on_delete=models.CASCADE)
    nom = models.CharField(max_length=100, blank=False , default=None, null=False)
    nombre_etudiant = models.IntegerField(blank=False , default=None , null=False)
    numero = models.IntegerField(blank=False , default=None , null=True)


    def __str__(self):
        return self.nom
    class Meta:
        verbose_name_plural = "groupe"


class Matier(models.Model):
    dep = models.ForeignKey(Departement,on_delete=models.CASCADE)
    nom = models.CharField(max_length=100, blank=False , default=None, null=False)

    #classe_etu = models.ManyToManyField(Classe)

    def __str__(self):
        return self.nom
    class Meta:
        verbose_name_plural = "matiére"


class Niveau(models.Model):
    nom = models.CharField(max_length=100, blank=False , default=None, null=False)

    def __str__(self):
        return self.nom
    class Meta:
        verbose_name_plural = "niveau"



class Professeur(models.Model):
    dep = models.ForeignKey(Departement, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100, blank=False , default=None, null=False)
    prenom = models.CharField(max_length=100, blank=False , default=None, null=False)
    email = models.CharField(max_length=255, blank=False , default=None, null=False)
    specialite = models.CharField(max_length=100, blank=False , default=None, null=False)
    mobile = models.CharField(max_length=100, blank=False , default=None, null=False)

    def __str__(self):
        return self.nom
    class Meta:
        verbose_name_plural = "professeur"


class Salle(models.Model):
    type = models.CharField(max_length=100, blank=False , default=None, null=False)
    capacite = models.CharField(max_length=100, blank=False , default=None, null=False)

    def __str__(self):
        return self.type
    class Meta:
        verbose_name_plural = "salle"

class CalandrierStandard(models.Model):
    nom = models.CharField(max_length=100, blank=False , default=None, null=False)

    def __str__(self):
        return 'calandrier standard'
    class Meta:
        verbose_name_plural = "Calandrier Standard"


class Jour(models.Model):
    nom = models.CharField(max_length=100, blank=False , default=None, null=False)
    numero = models.IntegerField(blank=False , default=None, null=False)

    def __str__(self):
        return self.nom
    class Meta:
        verbose_name_plural = "Jour"



class ExceptionCalandrier(models.Model):
    nom = models.CharField(max_length=100, blank=False , default=None, null=False)
    calandrier = models.ForeignKey(CalandrierStandard, on_delete=models.CASCADE)
    créneau = models.ManyToManyField(Creneau)
    date = models.DateField(blank=False , default=None, null=False)
    type = models.BooleanField()


    def __str__(self):
        return self.nom
    class Meta:
        verbose_name_plural = "éxception Calandrier"



class IndispoProf(models.Model):
    prof = models.ForeignKey(Professeur,on_delete=models.CASCADE)
    créneaux = models.ManyToManyField(Creneau)
    date = models.DateField(blank=False , default=None, null=False)

    def __str__(self):
        return '%s' %(self.prof.nom)
    class Meta:
        verbose_name_plural = "Indispo Prof"


class IndispoGroupe(models.Model):
    groupe = models.ForeignKey(Groupe,on_delete=models.CASCADE)
    créneaux = models.ManyToManyField(Creneau)
    date = models.DateField(blank=False , default=None, null=False)

    def __str__(self):
        return '%s' %(self.groupe.nom)
    class Meta:
        verbose_name_plural = "Indispo Groupe"


class Preferance_prof(models.Model):
    prof = models.ForeignKey(Professeur,on_delete=models.CASCADE)
    jour = models.ForeignKey(Jour,on_delete=models.CASCADE)
    créneaux = models.ManyToManyField(Creneau)

    def __str__(self):
        return '%s' %(self.prof.nom)
    class Meta:
        verbose_name_plural = "Préferance"


class DetailCalandrier(models.Model):
    calandrier = models.ForeignKey(CalandrierStandard, on_delete=models.CASCADE)
    jour = models.ForeignKey(Jour, on_delete=models.CASCADE)
    créneaux = models.ManyToManyField(Creneau)


    def __str__(self):
        return '%s' %(self.calandrier.nom)

    class Meta:
     #  unique_together = (('calandrier','jour'))
        verbose_name_plural = "Détail Calandrier"



class Seance(models.Model):
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    créneau = models.ForeignKey(Creneau, on_delete=models.CASCADE)
    date = models.DateField(blank=False , default=None, null=False)

    def __str__(self):
        return '%s' %(self.cours.nom)
    class Meta:
        unique_together = (('cours','créneau','date'))
        verbose_name_plural= "Seance"


class GroupeChevauchement(models.Model):
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    groupe1 = models.ForeignKey(Groupe, related_name="grp1", on_delete=models.CASCADE)
    groupe2 = models.ForeignKey(Groupe, related_name="grp2", on_delete=models.CASCADE)

    def __str__(self):
        return '%s' %(self.classe.nom)
    class Meta:
        unique_together = (('classe','groupe1','groupe2'))
        verbose_name_plural= "Groupe Chevauchement"

