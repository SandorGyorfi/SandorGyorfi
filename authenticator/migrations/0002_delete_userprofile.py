# Generated by Django 5.0.3 on 2024-04-09 19:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("authenticator", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="UserProfile",
        ),
    ]
