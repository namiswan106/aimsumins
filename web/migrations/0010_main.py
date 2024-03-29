# Generated by Django 4.2.7 on 2024-01-18 15:32

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0009_alter_portfolio_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Main",
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
                ("banner_title", models.CharField(max_length=200)),
                (
                    "banner_image",
                    versatileimagefield.fields.VersatileImageField(upload_to="main"),
                ),
                ("banner_description", models.TextField()),
                ("about_title", models.CharField(max_length=200)),
                (
                    "about_image",
                    versatileimagefield.fields.VersatileImageField(upload_to="main"),
                ),
                ("about_description", models.TextField()),
            ],
        ),
    ]
