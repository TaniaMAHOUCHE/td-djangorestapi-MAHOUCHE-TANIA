# Generated by Django 5.0.6 on 2024-06-26 12:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chercheur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='ProjetDeRecherche',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date_debut', models.DateField()),
                ('date_fin_prevue', models.DateField(blank=True, null=True)),
                ('chef_de_projet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projets_recherches', related_query_name='projet', to='projects.chercheur')),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('contenu', models.TextField()),
                ('date_publication', models.DateField()),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publications', related_query_name='publication', to='projects.chercheur')),
            ],
        ),
    ]
