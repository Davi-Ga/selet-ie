# Generated by Django 4.1 on 2022-11-10 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("empresa", "0007_rename_caracteristica_empresa_caracteristicas_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="empresa",
            name="caracteristicas",
            field=models.TextField(null=True),
        ),
    ]
