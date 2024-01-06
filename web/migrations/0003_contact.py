# Generated by Django 4.2.7 on 2024-01-06 19:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0002_portfoliocategory_portfolio"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=200)),
                ("subject", models.CharField(max_length=200)),
                ("message", models.TextField()),
            ],
        ),
    ]
