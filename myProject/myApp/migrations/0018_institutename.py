# Generated by Django 5.0.6 on 2024-09-22 11:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myApp", "0017_delete_intermediateeducationmodel"),
    ]

    operations = [
        migrations.CreateModel(
            name="InstituteName",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("address", models.CharField(blank=True, max_length=512)),
                ("city", models.CharField(blank=True, max_length=100)),
                ("state", models.CharField(blank=True, max_length=100)),
                ("postal_code", models.CharField(blank=True, max_length=20)),
                ("country", models.CharField(blank=True, max_length=100)),
                ("website", models.URLField(blank=True)),
                (
                    "established_year",
                    models.PositiveIntegerField(blank=True, null=True),
                ),
                ("contact_number", models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]
