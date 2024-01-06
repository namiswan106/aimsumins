# Generated by Django 4.2.7 on 2024-01-06 17:36

from django.db import migrations, models
import tinymce.models
import versatileimagefield.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
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
                ("title", models.CharField(max_length=200)),
                ("slug", models.SlugField(max_length=200, unique=True)),
                ("date", models.DateField(blank=True, null=True)),
                (
                    "image",
                    versatileimagefield.fields.VersatileImageField(upload_to="blogs"),
                ),
                ("description", tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name="Faq",
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
                ("question", models.CharField(max_length=200)),
                ("answer", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Service",
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
                ("title", models.CharField(max_length=200)),
                ("slug", models.SlugField(max_length=100, unique=True)),
                (
                    "image",
                    versatileimagefield.fields.VersatileImageField(
                        upload_to="services"
                    ),
                ),
                ("description", tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name="Testmonial",
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
                ("position", models.CharField(blank=True, max_length=200, null=True)),
                ("description", models.TextField()),
            ],
        ),
    ]