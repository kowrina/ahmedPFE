# Generated by Django 3.0.8 on 2020-08-06 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iscae_emploi', '0002_auto_20200806_0346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preferance',
            name='créneau',
        ),
        migrations.AddField(
            model_name='preferance',
            name='créneaux',
            field=models.ManyToManyField(to='iscae_emploi.Creneau'),
        ),
    ]
