# Generated by Django 4.1 on 2022-11-08 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("empresa", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="empresa",
            name="nicho",
            field=models.CharField(
                choices=[
                    ("M", "Marketing"),
                    ("N", "Nutrição"),
                    ("D", "Design"),
                    ("T", "Tecnologia"),
                    ("P", "Psicologia"),
                ],
                default=1,
                max_length=3,
            ),
            preserve_default=False,
        ),
    ]
