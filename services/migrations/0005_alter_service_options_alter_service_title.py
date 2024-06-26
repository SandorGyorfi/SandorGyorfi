# Generated by Django 5.0.3 on 2024-06-25 14:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("services", "0004_service_home_description"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="service",
            options={
                "ordering": ["title"],
                "verbose_name": "Service",
                "verbose_name_plural": "Services",
            },
        ),
        migrations.AlterField(
            model_name="service",
            name="title",
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
