# Generated by Django 5.0.6 on 2024-06-26 12:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projetderecherche',
            name='chef_de_projet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projets_recherches', related_query_name='projet', to='projects.chercheur'),
        ),
    ]
