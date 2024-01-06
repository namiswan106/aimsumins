# Generated by Django 4.2.7 on 2024-01-06 19:30

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0003_contact"),
    ]

    operations = [
        migrations.CreateModel(
            name="Client_logo",
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
                (
                    "image",
                    versatileimagefield.fields.VersatileImageField(
                        upload_to="client_logo"
                    ),
                ),
                ("name", models.CharField(max_length=200)),
            ],
        ),
    ]