# Generated by Django 4.2.1 on 2024-12-14 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_services", "0003_remove_services_time_serv"),
    ]

    operations = [
        migrations.AddField(
            model_name="services",
            name="min_serv",
            field=models.IntegerField(default=0),
        ),
    ]
