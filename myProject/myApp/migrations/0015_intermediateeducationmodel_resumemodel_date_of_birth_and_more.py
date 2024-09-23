# Generated by Django 5.0.6 on 2024-09-22 11:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myApp", "0014_intermediatelanguagemodel_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="IntermediateEducationModel",
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
                ("institution_name", models.CharField(max_length=100, null=True)),
                ("degree", models.CharField(max_length=100, null=True)),
                ("field_of_study", models.CharField(max_length=100, null=True)),
                ("start_date", models.DateField(blank=True, null=True)),
                ("end_date", models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name="resumemodel",
            name="date_of_birth",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name="EducationModel",
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
                ("institution_name", models.CharField(max_length=100, null=True)),
                ("degree", models.CharField(max_length=100, null=True)),
                ("field_of_study", models.CharField(max_length=100, null=True)),
                ("start_date", models.DateField(blank=True, null=True)),
                ("end_date", models.DateField(blank=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("user", "institution_name", "degree")},
            },
        ),
    ]