# Generated by Django 4.2.7 on 2024-02-14 16:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("job", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="location",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]