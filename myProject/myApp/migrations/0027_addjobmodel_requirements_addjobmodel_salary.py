# Generated by Django 5.0.6 on 2024-09-22 16:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myApp", "0026_remove_addjobmodel_end_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="addjobmodel",
            name="requirements",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="addjobmodel",
            name="salary",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
