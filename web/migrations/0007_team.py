# Generated by Django 4.2.7 on 2024-01-07 18:18

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0006_alter_blog_image_alter_service_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Team",
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
                ("position", models.CharField(max_length=200)),
                (
                    "image",
                    versatileimagefield.fields.VersatileImageField(upload_to="team"),
                ),
            ],
        ),
    ]
