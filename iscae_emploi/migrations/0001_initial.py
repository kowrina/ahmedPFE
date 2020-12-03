# Generated by Django 3.0.8 on 2020-11-30 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CalandrierStandard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default=None, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Calandrier Standard',
            },
        ),
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default=None, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'classe',
            },
        ),
        migrations.CreateModel(
            name='Creneau',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(default=None)),
                ('nom', models.CharField(default=None, max_length=100)),
                ('debut', models.TimeField(default=None, max_length=100)),
                ('fin', models.TimeField(default=None, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Créneau',
            },
        ),
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default=None, max_length=100)),
                ('chef', models.CharField(default=None, max_length=100)),
                ('email', models.EmailField(default=None, max_length=100)),
                ('mobile', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'departement',
            },
        ),
        migrations.CreateModel(
            name='Groupe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default=None, max_length=100)),
                ('nombre_etudiant', models.IntegerField(default=None)),
                ('numero', models.IntegerField(default=None, null=True)),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iscae_emploi.Classe')),
            ],
            options={
                'verbose_name_plural': 'groupe',
            },
        ),
        migrations.CreateModel(
            name='Jour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default=None, max_length=100)),
                ('numero', models.IntegerField(default=None)),
            ],
            options={
                'verbose_name_plural': 'Jour',
            },
        ),
        migrations.CreateModel(
            name='Niveau',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default=None, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'niveau',
            },
        ),
        migrations.CreateModel(
            name='Salle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default=None, max_length=100)),
                ('capacite', models.CharField(default=None, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'salle',
            },
        ),
        migrations.CreateModel(
            name='Professeur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default=None, max_length=100)),
                ('prenom', models.CharField(default=None, max_length=100)),
                ('email', models.CharField(default=None, max_length=255)),
                ('specialite', models.CharField(default=None, max_length=100)),
                ('mobile', models.CharField(default=None, max_length=100)),
                ('dep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iscae_emploi.Departement')),
            ],
            options={
                'verbose_name_plural': 'professeur',
            },
        ),
        migrations.CreateModel(
            name='Preferance_prof',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('créneaux', models.ManyToManyField(to='iscae_emploi.Creneau')),
                ('jour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iscae_emploi.Jour')),
                ('prof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iscae_emploi.Professeur')),
            ],
            options={
                'verbose_name_plural': 'Préferance',
            },
        ),
        migrations.CreateModel(
            name='Matier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default=None, max_length=100)),
                ('dep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iscae_emploi.Departement')),
            ],
            options={
                'verbose_name_plural': 'matiére',
            },
        ),
        migrations.CreateModel(
            name='IndispoProf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_debut', models.DateField(default=None)),
                ('date_fin', models.DateField(blank=True, default=True, null=True)),
                ('créneaux', models.ManyToManyField(to='iscae_emploi.Creneau')),
                ('jours', models.ManyToManyField(to='iscae_emploi.Jour')),
                ('prof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iscae_emploi.Professeur')),
            ],
            options={
                'verbose_name_plural': 'Indispo Prof',
            },
        ),
        migrations.CreateModel(
            name='IndispoGroupe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_debut', models.DateField(default=None)),
                ('date_fin', models.DateField(blank=True, default=True, null=True)),
                ('créneaux', models.ManyToManyField(to='iscae_emploi.Creneau')),
                ('groupe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iscae_emploi.Groupe')),
                ('jours', models.ManyToManyField(to='iscae_emploi.Jour')),
            ],
            options={
                'verbose_name_plural': 'Indispo Groupe',
            },
        ),
        migrations.CreateModel(
            name='Filier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default=None, max_length=100)),
                ('dep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iscae_emploi.Departement')),
            ],
            options={
                'verbose_name_plural': 'filiére',
            },
        ),
        migrations.CreateModel(
            name='ExceptionCalandrier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default=None, max_length=100)),
                ('date', models.DateField(default=None)),
                ('type', models.BooleanField()),
                ('calandrier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iscae_emploi.CalandrierStandard')),
                ('créneau', models.ManyToManyField(to='iscae_emploi.Creneau')),
            ],
            options={
                'verbose_name_plural': 'éxception Calandrier',
            },
        ),
        migrations.CreateModel(
            name='DetailCalandrier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calandrier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iscae_emploi.CalandrierStandard')),
                ('créneaux', models.ManyToManyField(to='iscae_emploi.Creneau')),
                ('jour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iscae_emploi.Jour')),
            ],
            options={
                'verbose_name_plural': 'Détail Calandrier',
            },
        ),
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default=None, max_length=100)),
                ('charge', models.IntegerField(default=None)),
                ('groupe', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='iscae_emploi.Groupe')),
                ('matier', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='iscae_emploi.Matier')),
                ('prof', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='iscae_emploi.Professeur')),
                ('salle', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='iscae_emploi.Salle')),
            ],
            options={
                'verbose_name_plural': 'cours',
            },
        ),
        migrations.AddField(
            model_name='classe',
            name='filier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iscae_emploi.Filier'),
        ),
        migrations.AddField(
            model_name='classe',
            name='matier_etu',
            field=models.ManyToManyField(to='iscae_emploi.Matier'),
        ),
        migrations.AddField(
            model_name='classe',
            name='niveau',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iscae_emploi.Niveau'),
        ),
        migrations.CreateModel(
            name='Seance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=None)),
                ('cours', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iscae_emploi.Cours')),
                ('créneau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iscae_emploi.Creneau')),
            ],
            options={
                'verbose_name_plural': 'Seance',
                'unique_together': {('cours', 'créneau', 'date')},
            },
        ),
        migrations.CreateModel(
            name='GroupeChevauchement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iscae_emploi.Classe')),
                ('groupe1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grp1', to='iscae_emploi.Groupe')),
                ('groupe2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grp2', to='iscae_emploi.Groupe')),
            ],
            options={
                'verbose_name_plural': 'Groupe Chevauchement',
                'unique_together': {('classe', 'groupe1', 'groupe2')},
            },
        ),
    ]