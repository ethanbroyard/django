# Generated by Django 4.2.5 on 2023-09-26 16:09

from django.db import migrations


def migrer_artiste(apps, schema):
    # On récupère les modèles
    Morceau = apps.get_model('musiques', 'Morceau')
    Artiste = apps.get_model('musiques', 'Artiste')
    artistes_connus = [fields['artiste']
                       for fields in Morceau.objects.all().values('artiste').distinct()]
    # On peuple la table Artiste
    for artiste in artistes_connus:
        Artiste.objects.create(nom=artiste)

def annuler_migrer_artiste(apps, schema):
    Artiste = apps.get_model('musiques', 'Artiste')
    Artiste.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('musiques', '0003_artiste'),
    ]

    operations = [
        migrations.RunPython(migrer_artiste,
                             reverse_code=annuler_migrer_artiste)
    ]