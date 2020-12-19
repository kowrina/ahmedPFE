from django import forms
from django.forms import DateInput

from .models import *


class DepartementForm(forms.ModelForm):

    class Meta:
        model = Departement
        fields = '__all__'


class SalleForm(forms.ModelForm):

    class Meta:
        model = Salle
        fields = '__all__'


class MatierForm(forms.ModelForm):

    class Meta:
        model = Matier
        fields = ['nom']


class ProfesseurForm(forms.ModelForm):

    class Meta:
        model = Professeur
        fields = ['nom','prenom','email','specialite','mobile']


class FilierForm(forms.ModelForm):

    class Meta:
        model = Filier
        fields = ['nom']


class ClasseForm(forms.ModelForm):

    class Meta:
        model = Classe
        fields = ['nom','niveau']


class JourForm(forms.ModelForm):

    class Meta:
        model = Jour
        fields = '__all__'


class CoursForm(forms.ModelForm):

    class Meta:
        model = Cours
        fields = ['nom','type','prof','matier','salle','charge']


class GroupeForm(forms.ModelForm):

    class Meta:
        model = Groupe
        fields = ['nom','nombre_etudiant']


class CreneauForm(forms.ModelForm):

    class Meta:
        model = Creneau
        fields = '__all__'

class DetailcalandrierForm(forms.ModelForm):

    class Meta:
        model = DetailCalandrier
        fields = ['jour','créneaux']

class ExceptioncalandrierForm(forms.ModelForm):

    class Meta:
        model = ExceptionCalandrier
        fields = ['nom','créneau','type']

class SeanceForm(forms.ModelForm):

    class Meta:
        model = Seance
        fields = ['cours','créneau']
        
        

class PreferanceprofForm(forms.ModelForm):

    class Meta:
        model = Preferance_prof
        fields = ['jour','créneaux']


class GroupeChevauchementForm(forms.ModelForm):

    class Meta:
        model = GroupeChevauchement
        fields = ['groupe1','groupe2']
        
    
    def __init__(self, pk, *args, **kwargs):
        super(GroupeChevauchementForm, self).__init__(*args, **kwargs)
        self.fields['groupe1'].queryset = Groupe.objects.filter(classe_id=pk)
        self.fields['groupe2'].queryset = Groupe.objects.filter(classe_id=pk)


class NiveauForm(forms.ModelForm):

    class Meta:
        model = Niveau
        fields ='__all__'

class IndispoprofForm(forms.ModelForm):

    class Meta:
        model = IndispoProf
        fields = ['jours','créneaux']
        date_debut = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        }))
        date_fin = forms.DateTimeField(
            input_formats=['%d/%m/%Y %H:%M'],
            widget=forms.DateTimeInput(attrs={
                'class': 'form-control datetimepicker-input',
                'data-target': '#datetimepicker2'
            }))

class IndispogroupeForm(forms.ModelForm):


    class Meta:
        model = IndispoGroupe
        fields = ['jours','créneaux']
        date_debut = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        }))
        date_fin = forms.DateTimeField(
            input_formats=['%d/%m/%Y %H:%M'],
            widget=forms.DateTimeInput(attrs={
                'class': 'form-control datetimepicker-input',
                'data-target': '#datetimepicker2'
            }))



class CalandrierForm(forms.ModelForm):

    class Meta:
        model = CalandrierStandard
        fields = '__all__'
