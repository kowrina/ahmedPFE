from django.db import models
from  django import forms
from django.contrib import admin
from django.contrib.admin import widgets
from django.utils.translation import ugettext_lazy as _
from searchableselect.widgets import SearchableSelect

from import_export.admin import ImportExportModelAdmin

from .models import  ExceptionCalandrier ,Preferance_prof,Professeur,Groupe,Departement,Matier,Salle,\
                     Classe,Cours,Filier,Niveau,Creneau,IndispoProf,Jour,\
                     CalandrierStandard,DetailCalandrier,Seance,IndispoGroupe,GroupeChevauchement

admin.site.register(ExceptionCalandrier)
admin.site.register(Preferance_prof)
admin.site.register(Salle)
#admin.site.register(Cours)
#admin.site.register(Classe)
admin.site.register(Filier)
admin.site.register(Niveau)
admin.site.register(Creneau)
admin.site.register(IndispoProf)
admin.site.register(IndispoGroupe)
admin.site.register(CalandrierStandard)
admin.site.register(DetailCalandrier)
admin.site.register(Seance)
admin.site.register(GroupeChevauchement)

@admin.register(Professeur)
class ProfesseurImportExport(ImportExportModelAdmin):
    pass

@admin.register(Matier)
class MatierImportExport(ImportExportModelAdmin):
    pass

@admin.register(Groupe)
class GroupeImportExport(ImportExportModelAdmin):
    pass

@admin.register(Departement)
class DepartementImportExport(ImportExportModelAdmin):
    pass

@admin.register(Jour)
class JourImportExport(ImportExportModelAdmin):
    pass

@admin.register(Cours)
class CoursImportExport(ImportExportModelAdmin):
    pass

@admin.register(Classe)
class ClasseImportExport(ImportExportModelAdmin):
    pass





