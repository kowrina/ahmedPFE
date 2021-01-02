from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
app_name='iscae_emploi'

urlpatterns = [
    path('login/',LoginView.as_view(template_name='user/login.html') , name='login'),
    path('logout/',LogoutView.as_view() , name='logout'),



    path('index/',views.index , name='index'),
    path('config/',views.config , name='config'),
    path('dp/',views.departement , name='dp'),
    path('Cours/',views.cours , name='cours'),
    path('salles/',views.salle , name='salle'),
    path('niveaux/',views.niveau , name='niveau'),
    path('jours/',views.jours , name='jours'),
    path('creneaux/',views.creneaux , name='creneaux'),
    path('calandriers/',views.calandriers , name='calandriers'),
    path('seances/<int:pk>/',views.seance , name='seances'),
    path('chevauch/<int:pk>/',views.chevauch , name='chevauch'),


    path('seance_download/',views.seance_download , name='seance_download'),
    path('emploi_download/',views.emploi_download , name='emploi_download'),


    #************* add object **************

    path('dep_ajout/',views.dep_ajout , name='dep_ajout'),
    path('dep_edit/<int:pk>/',views.dep_edit , name='dep_edit'),
    path('dep_delete/<int:pk>/',views.dep_delete , name='dep_delete'),

    path('creneau_ajout/',views.creneau_ajout , name='creneau_ajout'),
    path('creneau_edit/<int:pk>/',views.creneau_edit , name='creneau_edit'),
    path('creneau_delete/<int:pk>/',views.creneau_delete , name='creneau_delete'),

    path('cal_ajout/',views.calandrier_ajout , name='cal_ajout'),
    path('cal_edit/<int:pk>/',views.calandrier_edit , name='cal_edit'),
    path('cal_delete/<int:pk>/',views.calandrier_delete , name='cal_delete'),

    path('sall_ajout/',views.sall_ajout , name='sall_ajout'),
    path('sall_edit/<int:pk>/',views.sall_edit , name='sall_edit'),
    path('sall_delete/<int:pk>/',views.sall_delete , name='sall_delete'),

    path('seance_ajout/<int:pk>/',views.seance_ajout , name='seance_ajout'),
    path('seance_edit/<int:pk>/',views.seance_edit , name='seance_edit'),
    path('seance_delete/<int:pk>/',views.seance_delete , name='seance_delete'),

    path('matier_ajout/<int:pk>/',views.matier_ajout , name='matier_ajout'),
    path('matier_edit/<int:pk>/',views.matier_edit , name='matier_edit'),
    path('matier_delete/<int:pk>/',views.matier_delete , name='matier_delete'),

    path('prof_ajout/<int:pk>/',views.prof_ajout , name='prof_ajout'),
    path('prof_edit/<int:pk>/',views.prof_edit , name='prof_edit'),
    path('prof_delete/<int:pk>/',views.prof_delete , name='prof_delete'),

    path('filier_ajout/<int:pk>/',views.filier_ajout , name='filier_ajout'),
    path('filier_edit/<int:pk>/',views.filier_edit , name='filier_edit'),
    path('filier_delete/<int:pk>/',views.filier_delete , name='filier_delete'),

    path('classe_ajout/<int:pk>/',views.classe_ajout , name='classe_ajout'),
    path('classe_edit/<int:pk>/',views.classe_edit , name='classe_edit'),
    path('classe_delete/<int:pk>/',views.classe_delete , name='classe_delete'),

    path('joure_ajout/',views.joure_ajout , name='joure_ajout'),
    path('joure_edit/<int:pk>/',views.joure_edit , name='joure_edit'),
    path('joure_delete/<int:pk>/',views.joure_delete , name='joure_delete'),

    path('niveau_ajout/',views.niveau_ajout , name='niveau_ajout'),
    path('niveau_edit/<int:pk>/',views.niveau_edit , name='niveau_edit'),
    path('niveau_delete/<int:pk>/',views.niveau_delete , name='niveau_delete'),

    path('cours_ajout/<int:pk>/',views.cours_ajout , name='cours_ajout'),
    path('cours_edit/<int:pk>/',views.cours_edit , name='cours_edit'),
    path('cours_delete/<int:pk>/',views.cours_delete , name='cours_delete'),

    path('groupe_ajout/<int:pk>/',views.groupe_ajout , name='groupe_ajout'),
    path('groupe_edit/<int:pk>/',views.groupe_edit , name='groupe_edit'),
    path('groupe_delete/<int:pk>/',views.groupe_delete , name='groupe_delete'),

    path('detail_c_ajout/<int:pk>/',views.detail_c_ajout , name='detail_c_ajout'),
    path('detail_c_edit/<int:pk>/',views.detail_c_edit , name='detail_c_edit'),
    path('detail_c_delete/<int:pk>/',views.detail_c_delete , name='detail_c_delete'),

    path('prof_indispo_ajout/<int:pk>/',views.prof_indispo_ajout , name='prof_indispo_ajout'),
    path('prof_indispo_edit/<int:pk>/',views.prof_indispo_edit , name='prof_indispo_edit'),
    path('prof_indispo_delete/<int:pk>/',views.prof_indispo_delete , name='prof_indispo_delete'),

    path('prof_preferance_ajout/<int:pk>/',views.prof_preferance_ajout , name='prof_preferance_ajout'),
    path('prof_preferance_edit/<int:pk>/',views.prof_preferance_edit , name='prof_preferance_edit'),
    path('prof_preferance_delete/<int:pk>/',views.prof_preferance_delete , name='prof_preferance_delete'),

    path('groupe_indispo_ajout/<int:pk>/',views.groupe_indispo_ajout , name='groupe_indispo_ajout'),
    path('groupe_indispo_edit/<int:pk>/',views.groupe_indispo_edit , name='groupe_indispo_edit'),
    path('groupe_indispo_delete/<int:pk>/',views.groupe_indispo_delete , name='groupe_indispo_delete'),

    path('cal_exception_ajout/<int:pk>/',views.cal_exception_ajout , name='cal_exception_ajout'),
    path('cal_exception_edit/<int:pk>/',views.cal_exception_edit , name='cal_exception_edit'),
    path('cal_exception_delete/<int:pk>/',views.cal_exception_delete , name='cal_exception_delete'),

    path('chevauch_ajout/<int:pk>/',views.chevauch_ajout , name='chevauch_ajout'),
    path('chevauch_edit/<int:pk>/',views.chevauch_edit , name='chevauch_edit'),
    path('chevauch_delete/<int:pk>/',views.chevauch_delete , name='chevauch_delete'),



    # ##############end add object  ###############

    path('dep_matiers/<int:pk>/',views.dep_matiers , name='dep_matiers'),
    path('filier_classes/<int:pk>/',views.filier_classes , name='filier_classes'),
    path('classe_groupe/<int:pk>/',views.classe_groupe , name='classe_groupe'),
    path('classe_matiere/<int:pk>/',views.classe_matiere , name='classe_matiere'),

    path('groupe_cours/<int:pk>/',views.groupe_cours , name='groupe_cours'),
    path('groupe_indispo/<int:pk>/',views.groupe_indispo , name='groupe_indispo'),
    path('groupe_indispo_creneau/<int:pk>/',views.groupe_indispo_creneau , name='groupe_indispo_creneau'),
    path('groupe_indispo_jours/<int:pk>/',views.groupe_indispo_jours , name='groupe_indispo_jours'),
    path('prof_cours/<int:pk>/',views.prof_cours , name='prof_cours'),
    path('prof_indispo/<int:pk>/',views.prof_indispo , name='prof_indispo'),
    path('prof_indispo_creneau/<int:pk>/',views.prof_indispo_creneau , name='prof_indispo_creneau'),
    path('prof_indispo_jours/<int:pk>/',views.prof_indispo_jours , name='prof_indispo_jours'),
    path('prof_preferance/<int:pk>/',views.prof_preferance , name='prof_preferance'),
    path('detail_c/<int:pk>/',views.detail_c , name='detail_c'),
    path('filiere/<int:pk>/',views.filiere , name='filiere'),
    path('prof/<int:pk>/',views.prof , name='prof'),
    path('j_creneaux/<int:pk>/',views.j_creneaux , name='j_creneaux'),
    path('c_exception/<int:pk>/',views.c_exception , name='c_exception'),


    path('emploi/<int:pk>/',views.emploi , name='emploi'),


]


