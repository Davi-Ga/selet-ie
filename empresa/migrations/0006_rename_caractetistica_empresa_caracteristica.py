# Generated by Django 4.1 on 2022-11-08 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("empresa", "0005_rename_vagas_vaga"),
    ]

    operations = [
        migrations.RenameField(
            model_name="empresa",
            old_name="caractetistica",
            new_name="caracteristica",
        ),
    ]
