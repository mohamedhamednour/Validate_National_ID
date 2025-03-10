# Generated by Django 4.2.17 on 2025-01-10 23:03

from django.db import migrations, models
import egyptianidapp.mixinmodels


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="NationalID",
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
                ("number", models.CharField(max_length=14, unique=True)),
                ("birth_date", models.DateField(null=True)),
                ("location", models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                "verbose_name": "National ID",
                "verbose_name_plural": "National IDs",
            },
            bases=(egyptianidapp.mixinmodels.NationalIDMixin, models.Model),
        ),
        migrations.CreateModel(
            name="NationalIDLog",
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
                ("endpoint", models.CharField(max_length=255)),
                ("method", models.CharField(max_length=10)),
                ("status_code", models.PositiveIntegerField()),
                (
                    "response_data",
                    models.JSONField(blank=True, default=dict, null=True),
                ),
                ("request_data", models.JSONField(blank=True, default=dict, null=True)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
