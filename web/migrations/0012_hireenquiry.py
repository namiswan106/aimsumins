# Generated by Django 4.2.7 on 2024-02-14 19:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0011_alter_main_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="HireEnquiry",
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
                ("job", models.CharField(max_length=200)),
            ],
        ),
    ]
