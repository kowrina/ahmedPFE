# Generated by Django 3.0.8 on 2020-11-14 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iscae_emploi', '0014_groupe_numero'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cours',
            unique_together=set(),
        ),
    ]